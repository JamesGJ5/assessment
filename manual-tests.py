from answers import calculate_timespan_no_walktime
from answers import calculate_timespan_with_walktime
from answers import calculate_timespan_different_rates

print(calculate_timespan_no_walktime([], 1) == 0)
print(calculate_timespan_no_walktime([400, 750, 1000, 1500], 1) == 36.5)
print(calculate_timespan_no_walktime([400, 750, 1000, 1500], 2) == 22.5)
print(calculate_timespan_no_walktime([400, 750, 1000, 1500], 3) == 19)
print(calculate_timespan_no_walktime([300, 100, 200, 250, 50], 1) == 9)
print(calculate_timespan_no_walktime([300, 100, 200, 250, 50], 2) == 5.5)
print(calculate_timespan_no_walktime([300, 100, 200, 250, 50], 3) == 3.5)
print(calculate_timespan_no_walktime([300, 100, 200, 250, 50], 4) == 3)
print(calculate_timespan_no_walktime([300, 100, 200, 250, 50], 5) == 3)

print(calculate_timespan_with_walktime([], 1, 100) == 0)
print(calculate_timespan_with_walktime([400, 750, 1000, 1500], 1, 5) == 56.5)
print(calculate_timespan_with_walktime([400, 750, 1000, 1500], 2, 4) == 30.5)
print(calculate_timespan_with_walktime([400, 750, 1000, 1500], 3, 0) == 19)
print(calculate_timespan_with_walktime([300, 100, 200, 250, 50], 1, 3.5) == 26.5)
print(calculate_timespan_with_walktime([300, 100, 200, 250, 50], 2, 1) == 7.5)
print(calculate_timespan_with_walktime([300, 100, 200, 250, 50], 3, 1) == 5.5)
print(calculate_timespan_with_walktime([300, 100, 200, 250, 50], 4, 2) == 5.5)
print(calculate_timespan_with_walktime([300, 100, 200, 250, 50], 5, 3) == 6)

print(calculate_timespan_different_rates([], [100, 50, 20]) == 0)
print(calculate_timespan_different_rates([400, 750, 1000, 1500], [100]) == 36.5)
print(calculate_timespan_different_rates([400, 750, 1000, 1500], [100, 100]) == 22.5)
print(calculate_timespan_different_rates([400, 750, 1000, 1500], [100, 10]) == 75)
