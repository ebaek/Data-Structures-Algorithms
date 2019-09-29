# 210: Course Schedule II

from collections import defaultdict


from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseGraph = defaultdict(set)
        prereqDegrees = defaultdict(int)

        for course, prereq in prerequisites:
            courseGraph[prereq].add(course)
            prereqDegrees[course] += 1

        for course in range(numCourses):
            if course not in courseGraph:
                courseGraph[course]
            if course not in prereqDegrees:
                prereqDegrees[course]

        validCourses = []
        courseOrders = []

        for course, numRequirements in prereqDegrees.items():
            if numRequirements == 0:
                validCourses.append(course)

        while validCourses:
            takenCourse = validCourses.pop(0)
            courseOrders.append(takenCourse)

            for dependentCourse in courseGraph[takenCourse]:
                prereqDegrees[dependentCourse] -= 1

                if prereqDegrees[dependentCourse] == 0:
                    validCourses.append(dependentCourse)

        return courseOrders if len(courseOrders) == numCourses else []
