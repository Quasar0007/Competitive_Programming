class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        top = sandwiches[0]
        while students.count(top)>0:
            s_top = students[0]
            while top!=s_top:
                students.append(s_top)
                students.remove(s_top)
                s_top = students[0]
            
            sandwiches.remove(top)
            students.remove(s_top)
            if sandwiches:
                top = sandwiches[0]
            else:
                break
        return len(students)