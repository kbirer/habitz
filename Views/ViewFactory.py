from Views.AddOrUpdateHabitView import AddOrUpdateHabitView
from Views.AnalyticsView import AnalyticsView
from Views.CheckoutHabitView import CheckoutHabitView
from Views.HabitStreakView import HabitStreakView
from Views.ListCheckedoutHabitsView import ListCheckedoutHabitsView
from Views.ListHabitsView import ListHabitsView
from Views.MainView import MainView
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import ViewKeys


class ViewFactory():
    
    @staticmethod
    def NavigateToView(action: ViewAction) -> View:
        match action.NextViewId:
            case ViewKeys.ListHabits:
                return ListHabitsView(action)
            case ViewKeys.AddOrUpdateHabit:
                return AddOrUpdateHabitView(action)
            case ViewKeys.ListCheckedOutHabits:
                return ListCheckedoutHabitsView(action)
            case ViewKeys.CheckOutHabit:
                return CheckoutHabitView(action)
            case ViewKeys.Analytics:
                return AnalyticsView(action)
            case ViewKeys.HabitsWithLongestStreak:
                return HabitStreakView(action)
            case ViewKeys.Main:
                return MainView()
            case _:
                raise Exception(f'View not recognized {action.NextViewId}')
            
    
