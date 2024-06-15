class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of tuples, where each tuple contains the capital needed and the profit for each project
        projects = [(capital[i], profits[i]) for i in range(len(capital))]

        # Sort the projects by the capital needed
        projects.sort()

        # Create a max heap to store the profits of the projects that can be done with the current capital
        max_heap = []

        # Index to iterate over the projects
        i = 0

        # Do k projects
        for _ in range(k):
            # Add all the projects that can be done with the current capital to the max heap
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # If there are no projects that can be done with the current capital, return the current capital
            if not max_heap:
                return w

            # Pick the project with the maximum profit from the max heap and add its profit to the current capital
            w -= heapq.heappop(max_heap)

        return w