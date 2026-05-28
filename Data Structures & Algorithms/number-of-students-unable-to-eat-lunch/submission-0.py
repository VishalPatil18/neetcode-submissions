class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Understand:
            - 0: circular sandwiches
            - 1: square sandwiches
            - No. of sand = no. of students
            - if found, take and leave, if not go to the end of queue
            - students: queue, sandwiches: stack
        Input:
            - 2 arrays: students[] and sandwiches[]
            - i = 0 top of stack
            - j = 0 front of queue
        Output: Int (no. of students unable to eat, size of queue if stuck)
        Plan:
            - Check the front of queue and top of stack
                - if equal: remove both from queue and stack
                - if not: remove from queue front and move to back
                    - start counting the iterations
                    - if iterations <= length: iterate
                    - else return the length
                - if queue becomes empty return 0
        """
        itr = 0
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                itr = 0
            else:
                students.append(students.pop(0))
                itr += 1
                if itr > len(students):
                    return len(students)
        return 0
