# NOTE: please see ./important-notes-and-assumptions.md

from typing import Any, List, Union
import heapq

# === Internal Functions ===:
def _get_overall_timespan(
    tap_heap: List[Union[int, float]]
    ) -> Union[int, float]:

    return max(tap[0] for tap in tap_heap)


def _push_to_tap_heap(
    tap_heap: List[Union[int, float]], tap: List[Union[int, float]]
    ) -> None:

    heapq.heappush(tap_heap, tap)


def _update_tap_timespan(
    tap: List[Union[int, float]], time_for_bottle: float
    ) -> None:

    tap[0] = tap[0] + time_for_bottle


def _calculate_fill_time(
    bottle_size: int, tap_flow_rate: Union[int, float]
    ) -> float:

    return bottle_size / tap_flow_rate


def _calculate_time_for_bottle(
    bottle_size: int, tap_flow_rate: Union[int, float], walktime: Union[int, float]
    ) -> float:

    return _calculate_fill_time(bottle_size, tap_flow_rate) + walktime


def _extract_next_available_tap(
    tap_heap: List[List[Union[int, float]]]
    ) -> List[Union[int, float]]:

    # This returns the tap at the root of the heap, notably that with the smallest 
    # cumulative allotted timespan and thus which can be available next. If there are 
    # multiple available, the available tap with the lowest index is chosen, this 
    # justified in the docstring for calculate_timespan_different_rates.
    return heapq.heappop(tap_heap)


def _update_tap_heap(
    tap_heap: List[List[Union[int, float]]], bottle_size: int, walktime: Union[int, float]
    ) -> None:

    chosen_tap = _extract_next_available_tap(tap_heap)
    time_for_bottle = _calculate_time_for_bottle(bottle_size, tap_flow_rate=chosen_tap[2], walktime=walktime)
    _update_tap_timespan(chosen_tap, time_for_bottle)
    _push_to_tap_heap(tap_heap, chosen_tap)


def _make_tap(
    cumulative_timespan: Union[int, float],
    tap_index: int,
    flow_rate: Union[int, float]
    ) -> List[Union[int, float]]:
    """
    - Returns a list in which the first element is the tap's allotted timespan so far 
    (initially 0), the second its index and the third element its flowrate.
    See the docstring for calculate_timespan_different_rates for the importance
    of the tap index.   
    """

    # Representing taps as objects could lead to more understandable code but 
    # the assignment just mentions functions so I'll stick to procedural 
    # programming rather than object-oriented programming.
    return [cumulative_timespan, tap_index, flow_rate]

def _make_tap_list(
    tap_rate_list: List[Union[int, float]]
    ) -> List[List[Union[int, float]]]:

    return [_make_tap(0, tap_index, tap_rate) for tap_index, tap_rate in enumerate(tap_rate_list)]

def _make_tap_heap(
    tap_rate_list: List[Union[int, float]]
    ) -> List[List[Union[int, float]]]:

    tap_list = _make_tap_list(tap_rate_list)
    heapq.heapify(tap_list)
    return tap_list

def _calculate_overall_timespan(
    bottle_size_queue: List[int], tap_rate_list: List[Union[int, float]], walktime: Union[int, float]
    ) -> Union[int, float]:

    tap_heap = _make_tap_heap(tap_rate_list)
    for size in bottle_size_queue:
        _update_tap_heap(tap_heap, size, walktime)
    return _get_overall_timespan(tap_heap)


def _get_tap_flow_rate() -> Union[float, int]:
    """
    Just for use by the first two functions asked for.
    """

    return 100


def _make_tap_rate_list(
    number_of_taps: int
    ) -> List[Union[int, float]]:
    """
    Just for use by the first two functions asked for.
    """

    tap_flow_rate = _get_tap_flow_rate()
    return [tap_flow_rate] * number_of_taps


def _validate_number_of_taps(
    number_of_taps: Any
    ) -> bool:

    # Assuming there must be at least one tap, otherwise might have 
    # to make the decision of whether the bottles take a time of infinity
    # to be filled; infinity is not an integer like the assignment 
    # requires.
    return type(number_of_taps) == int and number_of_taps > 0


def _validate_every_bottle_size(
    bottle_size_queue: Any
    ) -> bool:

    for size in bottle_size_queue:
        # Asserting that bottle sizes are integers to align with the 
        # wording of the question.
        # Asserting that people can't be recorded to have bottles 
        # with a size of 0 or less.
        if type(size) != int or size <= 0:
            return False
    return True


def _validate_bottle_size_queue(
    bottle_size_queue: Any
    ) -> bool:

    # Other Python types, like tuple, are array-like as well but heapq only 
    # works on mutable arrays like a list, hence the type-check below only permitting 
    # the list type.
    return type(bottle_size_queue) == list and _validate_every_bottle_size(bottle_size_queue)


def _validate_inputs(
    bottle_size_queue: Any, number_of_taps: Any
    ) -> bool:

    return (_validate_bottle_size_queue(bottle_size_queue) and _validate_number_of_taps(number_of_taps))


# === Functions Being Requested ===
def calculate_timespan_no_walktime(
    bottle_size_queue: List[int], number_of_taps: int
    ) -> Union[int, float]:
    """
    - Function required by Part 1 of the assignment (initial task plus 
    first Bonus Points task).
    """

    assert _validate_inputs(bottle_size_queue, number_of_taps)
    tap_rate_list = _make_tap_rate_list(number_of_taps)
    return _calculate_overall_timespan(bottle_size_queue, tap_rate_list, walktime=0)


def calculate_timespan_with_walktime(
    bottle_size_queue: List[int], number_of_taps: int, walktime: Union[int, float]
    ) -> Union[int, float]:
    """
    - Function required by the second Bonus Points task.
    - Assumes initial people start at the queue and have to walk to the 
    tap and no one starts to walk to a tap unless it is free.
    """

    assert _validate_inputs(bottle_size_queue, number_of_taps)
    tap_rate_list = _make_tap_rate_list(number_of_taps)
    return _calculate_overall_timespan(bottle_size_queue, tap_rate_list, walktime)


def calculate_timespan_different_rates(
    bottle_size_queue: List[int], tap_rate_list: List[Union[int, float]]
    ) -> Union[int, float]:
    """
    - Function required by the third Bonus Points task.
    - Assuming multiple tap rates, all floats > 0.
    - Assuming bottle sizes > 0.
    - NOTE: when multiple taps are available at the same time, the tap chosen 
    for the next person is determined by which of those occurs earlier in 
    tap_rate_list, now treating that as a queue. That is why _make_tap_list 
    returns, for each tap, a list containing the tap_index as the second 
    parameter, so that the earliest of multiple taps available at the same 
    time is chosen next by the heap operations. This order was chosen as 
    a reference and a reference was needed because flow rates are different 
    now, the choice of which available tap to use affects the final timespan.
    """

    return _calculate_overall_timespan(bottle_size_queue, tap_rate_list, walktime=0)


# === For Manual Testing In ./manual-tests.py ===
__all__ = [
    "calculate_timespan_no_walktime",
    "calculate_timespan_with_walktime",
    "calculate_timespan_different_rates"
]


# === For Bonus Point 4 ===

# - I think the answer is yes--if the rate of at least one tap is
# increased, calculate_timespan_different_rates might output a larger number.

# - For example, say there are 2 taps, Tap 1 and Tap 2. Say that Tap 1 has a 
# significantly higher flow rate than Tap 2.

# - Initially, say there are 3 people in the queue and the front 2 immediately start 
# filling up their water bottles.

# - Say it takes less time for Person 1 to fill up their bottle (at Tap 1) than it 
# takes Person 2. As a result, Person 3 will follow Person 1 in using Tap 1.

# - Now, say that if the flow rate of Tap 2 is raised sufficiently, Person 2 instead 
# takes slightly less time than Person 1. Therefore, Person 3 will follow Person 2 in 
# using Tap 2.

# - If the flow rate Tap 2 had to be raised to in order to make this transition (from 
# Person 3 using Tap 1 to using Tap 2) was still lower than the flow rate of Tap 1, 
# Person 3 would take longer on Tap 2 than they would have on Tap 1.

# - Therefore, since at the transition point both Person 1 and Person 2 spend the 
# same time at their respective taps, now that Person 3 is using Tap 2 rather than 
# Tap 1, they are finishing later and thus the timespan is longer overall.

# - Here's an example:

if __name__ == "__main__":

    bottle_size_queue = [100, 75, 150]
    tap_rate_list_initially = [100, 50]
    tap_rate_list_after_increase = [100, 76]
    print(
        calculate_timespan_different_rates(
            bottle_size_queue, tap_rate_list_initially
        )
        <
        calculate_timespan_different_rates(
            bottle_size_queue, tap_rate_list_after_increase
        )
    )
