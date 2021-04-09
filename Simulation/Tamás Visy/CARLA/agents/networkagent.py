import random

from Networks.SCNN import SCNN
from ReinforcementModel import ReinforcementModel, AGENT_IM_WIDTH, AGENT_IM_HEIGHT
from agents.agent import Agent
from agents.state import feature_dimension
from support.logger import logger

feature_dimension = feature_dimension()
AGENT_MODEL_PATH = 'files/tensor.pt'
MODEL_TYPE = SCNN


class NetworkAgent(Agent):

    def __init__(self):
        super().__init__()

        self.choices = choices

        self.model = ReinforcementModel(dim_features=feature_dimension, height=AGENT_IM_HEIGHT,
                                        width=AGENT_IM_WIDTH, n_actions=ACTIONS_NUM, model=MODEL_TYPE)

    def predict(self, state):
        if state is None:
            return None, None
        action = self.model.predict(state)
        try:
            # Copy value, not reference
            choice = self.choices[action][:]
            # TODO (7) remove noise of agent out
            choice[1] += -0.05 + random.random() / 10

            # TODO (6) remove cheats
            if action is 0:
                choice[1] *= -1 * state.side
            if action is 1:
                choice[1] *= 1 * state.side

            return action, choice
        except RuntimeError:
            logger.error(f'Error when trying to find right value for {action}')
            return None, None

    def optimize(self, new_state, prev_state=None, action=None):
        try:
            return self.model.optimize(new_state, prev_state, action)
        except RuntimeError as r:
            logger.error(f'Error in model.optimize: {r}')

    def save(self, path=AGENT_MODEL_PATH):
        logger.info(f'Saving model to {path}')
        self.model.save_model(path)

    def load(self, path=AGENT_MODEL_PATH):
        logger.info(f'Loading model from {path}')
        try:
            self.model.load_model(path, dim_features=feature_dimension, image_height=AGENT_IM_HEIGHT,
                                  image_width=AGENT_IM_WIDTH, n_actions=ACTIONS_NUM, model=MODEL_TYPE)
        except FileNotFoundError as f:
            logger.error(f'Failed to find file at {path} - {f}')
        except RuntimeError as r:
            logger.critical(f'Failed to load agent from {path} - {r}')
