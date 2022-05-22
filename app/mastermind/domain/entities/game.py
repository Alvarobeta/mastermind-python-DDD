import logging
import json

import uuid
from enum import Enum
from typing import List
from app.mastermind.application.exceptions.end_game_exception import EndGameException

from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.entities.guess_colour import GuessColour
# from app.mastermind.application.exceptions.wrong_game_status_exception import WrongGameStatusException
from app.mastermind.application.exceptions.wrong_game_status_exception import WrongGameStatusException

logger = logging.getLogger(__name__)

class GAME_STATUS(str, Enum):
    PLAYING = "Playing"
    WON = "Won"
    LOST = "Lost"


class Game:
    id: str
    code: List[GuessColour]
    attempts: str
    status: GAME_STATUS
    feedbacks: str

    CODE_LENGTH: int = 4
    GAME_LIMIT: int = 8

    # MAX_ATTEMPTS: ClassVar[int] = int(os.environ["DEFAULT_MAX_ATTEMPTS"])
    # CODE_LENGTH: ClassVar[int] = int(os.environ["DEFAULT_CODE_LENGTH"])

    def __init__(
        self, 
        code: List[GuessColour], 
        id: str = str(uuid.uuid4()),
        attempts: str = '[]',
        feedbacks: str = '[]',
        status: GAME_STATUS = GAME_STATUS.PLAYING
    ) -> None:
        self.id = id
        self.code = code
        self.attempts = attempts
        self.feedbacks = feedbacks
        self.status = status

    def __str__(self) -> str:
        return f"Game(id={self.id}, code={self.code}, attempts={self.attempts}, feedbacks={self.feedbacks}, status={self.status})"

    def make_guess(self, guess: List[GuessColour]):
        if (self.status != GAME_STATUS.PLAYING):
            raise WrongGameStatusException(message=F'You cannot play. Status is {self.status}') 
        
        logger.debug(f" -------------- make_guess() guess={guess} --------------")

        attempts_list: List[List[GuessColour]] = []
        attempts_list = json.loads(self.attempts)
        attempts_list.append(guess)
        self.attempts = json.dumps(attempts_list)
        
        # compute last feedback
        feedback = self.compute_last_feedback(guess)

        logger.debug(f" -------------- make_guess() feedback={feedback} --------------")

        feedbacks_list: List[List[FeedbackColour]] = []
        feedbacks_list = json.loads(self.feedbacks)
        feedbacks_list.append(feedback)
        self.feedbacks = json.dumps(feedbacks_list)

        logger.debug(f" -------------- make_guess() self={self} --------------")

        # Win condition
        if all(f == FeedbackColour.BLACK for f in feedback):
            self.status = GAME_STATUS.WON

        # Lose condition
        if len(attempts_list) >= Game.GAME_LIMIT:
            self.status = GAME_STATUS.LOST


    def compute_last_feedback(self, guess: List[GuessColour]) -> List[FeedbackColour]:
        feedback: List[FeedbackColour] = []

        for index, colour in enumerate(guess):
            if any(colour == c for c in self.code):
                if guess[index] == self.code[index]:
                    feedback.append(FeedbackColour.BLACK)

                else:
                    feedback.append(FeedbackColour.WHITE)

                self.code[
                    index
                ] = GuessColour.EMPTY  # avoid erroneous comparisons on repeated colors

            else:
                feedback.append(FeedbackColour.EMPTY)
        
        return feedback
