class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        answer = [0] * n
        enter = []
        exit = []

        # Separate entering and exiting persons
        for i in range(n):
            if state[i] == 0:
                enter.append(i)
            else:
                exit.append(i)

        enter_ptr = 0
        exit_ptr = 0
        prev_action = -1
        time = 0

        # Iterate until both pointers reach the end
        while enter_ptr < len(enter) or exit_ptr < len(exit):
            # Check rules for entering and exiting persons
            if (enter_ptr < len(enter) and exit_ptr < len(exit) and
                arrival[enter[enter_ptr]] <= time and arrival[exit[exit_ptr]] <= time):
                if prev_action == 0:
                    answer[enter[enter_ptr]] = time
                    enter_ptr += 1
                    prev_action = 0
                else:
                    answer[exit[exit_ptr]] = time
                    exit_ptr += 1
                    prev_action = 1
            elif enter_ptr < len(enter) and arrival[enter[enter_ptr]] <= time:
                answer[enter[enter_ptr]] = time
                enter_ptr += 1
                prev_action = 0
            elif exit_ptr < len(exit) and arrival[exit[exit_ptr]] <= time:
                answer[exit[exit_ptr]] = time
                exit_ptr += 1
                prev_action = 1
            else:
                prev_action = -1

            time += 1

        return answer

