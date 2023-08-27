#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
<<<<<<< HEAD
        review_id (str): The Place id.
=======
        review_id (str): The review id.
>>>>>>> b406b7cee534a20d3d74063293f16e666e8c8124
        user_id (str): The User id.
        text (str): The text of the review.
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize clss user with kwargs
            Args:
                *args(positional arg): strings
                **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.review_id = ""
        self.user_id = ""
        self.text = ""
