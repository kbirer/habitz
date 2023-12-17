class ViewKeys:
    """Class which contains constant unique view ids"""
    main: str = 'Main'
    list_habits: str = 'ListHabits'
    add_or_update_habit: str = 'AddOrUpdateHabit'
    list_checked_out_habits: str = 'ListCheckedOutHabits'
    check_out_habit: str = 'CheckOutHabit'
    analytics: str = 'Analytics'
    habits_with_longest_streak: str = 'HabitsWithLongestStreak'


class MenuKeys:
    """Class which contains constant unique menu ids to display within a view"""
    update_habit: str = 'UpdateHabit'
    add_new_habit: str = 'AddNewHabit'
    habits_with_longest_streak: str = 'HabitsWithLongestStreak'
    longest_streak_of_selected_habit: str = 'LongestStreakOfSelectedHabit'
    back: str = 'Back'
