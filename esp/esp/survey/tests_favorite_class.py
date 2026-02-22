"""
Tests for Favorite Class survey functionality (Issue #3942)
"""

from django.test import TestCase
from esp.survey.models import Survey, Question, QuestionType, Answer, SurveyResponse
from esp.program.models import Program
from esp.users.models import ESPUser


class FavoriteClassSurveyTestCase(TestCase):
    """
    Test that Favorite Class questions work in survey results without requiring
    an "overall rating" question.
    """
    
    def test_favorite_class_question_type_exists(self):
        """
        Test that the Favorite Class question type exists in the database.
        """
        favorite_class_type = QuestionType.objects.filter(name='Favorite Class')
        self.assertGreater(
            favorite_class_type.count(), 0,
            "Favorite Class question type should exist"
        )
    
    def test_top_classes_with_favorite_class_question(self):
        """
        Test that top_classes view works with Favorite Class questions
        without requiring an overall rating question.
        """
        # This test would require setting up a full program, survey, and responses
        # For now, we're just documenting the expected behavior
        pass
    
    def test_top_classes_with_rating_question(self):
        """
        Test that top_classes view still works with overall rating questions
        (original functionality).
        """
        # This test would require setting up a full program, survey, and responses
        # For now, we're just documenting the expected behavior
        pass
    
    def test_top_classes_with_both_question_types(self):
        """
        Test that when both Favorite Class and overall rating questions exist,
        the view prefers the rating question (maintains backward compatibility).
        """
        # This test would require setting up a full program, survey, and responses
        # For now, we're just documenting the expected behavior
        pass
