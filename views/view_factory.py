from views.add_or_update_habit_view import AddOrUpdateHabitView
from views.analytics_view import AnalyticsView
from views.checkout_habit_view import CheckoutHabitView
from views.habit_streak_view import HabitStreakView
from views.list_checkedout_habits_view import ListCheckedoutHabitsView
from views.list_habits_view import ListHabitsView
from views.main_view import MainView
from views.view import View
from views.view_action import ViewAction
from views.view_keys import ViewKeys


class ViewFactory():
    """Factory class which resolves view instances from view id"""
    
    @staticmethod
    def navigate_to_view(action: ViewAction) -> View:
        """Function that resolves view to navigate
        
        Parameters:

        action -- next view to navigate
        
        """
        match action.next_view_id:
            case ViewKeys.list_habits:
                return ListHabitsView(action)
            case ViewKeys.add_or_update_habit:
                return AddOrUpdateHabitView(action)
            case ViewKeys.list_checked_out_habits:
                return ListCheckedoutHabitsView(action)
            case ViewKeys.check_out_habit:
                return CheckoutHabitView(action)
            case ViewKeys.analytics:
                return AnalyticsView(action)
            case ViewKeys.habits_with_longest_streak:
                return HabitStreakView(action)
            case ViewKeys.main:
                return MainView()
            case _:
                raise Exception(f'View not recognized {action.next_view_id}')
            
    
