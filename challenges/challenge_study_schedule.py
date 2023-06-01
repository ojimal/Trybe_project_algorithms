def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for period in permanence_period:
        start, end = period
        if not (isinstance(start, int) and isinstance(end, int)):
            return None
        if start <= target_time <= end:
            counter += 1
    return counter
