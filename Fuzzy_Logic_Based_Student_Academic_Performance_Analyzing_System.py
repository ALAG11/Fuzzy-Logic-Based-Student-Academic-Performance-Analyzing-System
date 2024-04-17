# Defining and importing necessary libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Defining the linguistic variables
STUDENT_ATTENDANCE = 'Student_Attendance'
STUDENT_PERFORMANCE = 'Student_Performance'
STUDENT_INTERNAL_MARKS = 'Student_Internal_Marks'
STUDENT_EXTERNAL_MARKS = 'Student_External_Marks'

# Defining the membership functions for the linguistic variables
POOR = 'Poor'
AVERAGE = 'Average'
GOOD = 'Good'
VERY_GOOD = 'Very_Good'
EXCELLENT = 'Excellent'

low_parameter = [0, 0, 40, 50]
average_parameter = [30, 40, 50, 60]
good_parameter = [40, 50, 60, 70]
very_good_parameter = [50, 60, 70, 80]
excellent_parameter = [65, 80, 100, 100]

# Function to compute the student performance using fuzzy logic defined
def compute_student_performance(student_attendance, student_internal_marks, student_external_marks):

    # Defining the antecedents and consequent
    internal_marks = ctrl.Antecedent(np.arange(0, 105, 5), STUDENT_INTERNAL_MARKS)
    attendance = ctrl.Antecedent(np.arange(0, 105, 5), STUDENT_ATTENDANCE)
    external_marks = ctrl.Antecedent(np.arange(0, 105, 5), STUDENT_EXTERNAL_MARKS)
    student_performance = ctrl.Consequent(np.arange(0, 105, 5), STUDENT_PERFORMANCE)

    # Setting the membership functions for the linguistic variables
    internal_marks[POOR] = fuzz.trapmf(internal_marks.universe, low_parameter)
    internal_marks[AVERAGE] = fuzz.trapmf(internal_marks.universe, average_parameter)
    internal_marks[GOOD] = fuzz.trapmf(internal_marks.universe, good_parameter)
    internal_marks[VERY_GOOD] = fuzz.trapmf(internal_marks.universe, very_good_parameter)
    internal_marks[EXCELLENT] = fuzz.trapmf(internal_marks.universe, excellent_parameter)

    attendance[POOR] = fuzz.trapmf(attendance.universe, [0, 0, 45, 55])
    attendance[AVERAGE] = fuzz.trapmf(attendance.universe, [35, 45, 55, 65])
    attendance[GOOD] = fuzz.trapmf(attendance.universe, [45, 55, 65, 75])
    attendance[VERY_GOOD] = fuzz.trapmf(attendance.universe, [55, 65, 75, 85])
    attendance[EXCELLENT] = fuzz.trapmf(attendance.universe, [65, 75, 100, 100])

    external_marks[POOR] = fuzz.trapmf(external_marks.universe, low_parameter)
    external_marks[AVERAGE] = fuzz.trapmf(external_marks.universe, average_parameter)
    external_marks[GOOD] = fuzz.trapmf(external_marks.universe, good_parameter)
    external_marks[VERY_GOOD] = fuzz.trapmf(external_marks.universe, very_good_parameter)
    external_marks[EXCELLENT] = fuzz.trapmf(external_marks.universe, excellent_parameter)

    student_performance[POOR] = fuzz.trapmf(student_performance.universe, low_parameter)
    student_performance[AVERAGE] = fuzz.trapmf(student_performance.universe, average_parameter)
    student_performance[GOOD] = fuzz.trapmf(student_performance.universe, good_parameter)
    student_performance[VERY_GOOD] = fuzz.trapmf(student_performance.universe, very_good_parameter)
    student_performance[EXCELLENT] = fuzz.trapmf(student_performance.universe, excellent_parameter)

    # Defining the fuzzy rules
    rule1 = ctrl.Rule(attendance[POOR] & external_marks[POOR] & internal_marks[POOR], student_performance[POOR])
    rule2 = ctrl.Rule(attendance[POOR] & external_marks[AVERAGE] & internal_marks[POOR], student_performance[POOR])
    rule3 = ctrl.Rule(attendance[POOR] & external_marks[GOOD] & internal_marks[POOR], student_performance[AVERAGE])
    rule4 = ctrl.Rule(attendance[POOR] & external_marks[VERY_GOOD] & internal_marks[POOR], student_performance[AVERAGE])
    rule5 = ctrl.Rule(attendance[POOR] & external_marks[GOOD] & internal_marks[VERY_GOOD], student_performance[GOOD])
    rule6 = ctrl.Rule(attendance[POOR] & external_marks[POOR] & internal_marks[AVERAGE], student_performance[POOR])
    rule7 = ctrl.Rule(attendance[POOR] & external_marks[AVERAGE] & internal_marks[AVERAGE], student_performance[AVERAGE])
    rule8 = ctrl.Rule(attendance[POOR] & external_marks[GOOD] & internal_marks[AVERAGE], student_performance[AVERAGE])
    rule9 = ctrl.Rule((attendance[POOR] & external_marks[GOOD] & internal_marks[GOOD]), student_performance[GOOD])
    rule10 = ctrl.Rule(attendance[POOR] & external_marks[EXCELLENT] & internal_marks[GOOD], student_performance[VERY_GOOD])
    rule11 = ctrl.Rule(attendance[AVERAGE] & external_marks[AVERAGE] & internal_marks[GOOD], student_performance[AVERAGE])
    rule12 = ctrl.Rule(attendance[AVERAGE] & external_marks[GOOD] & internal_marks[GOOD], student_performance[GOOD])
    rule13 = ctrl.Rule(attendance[AVERAGE] & external_marks[VERY_GOOD] & internal_marks[GOOD], student_performance[GOOD])
    rule14 = ctrl.Rule(attendance[AVERAGE] & external_marks[VERY_GOOD] & internal_marks[VERY_GOOD], student_performance[VERY_GOOD])
    rule15 = ctrl.Rule(attendance[AVERAGE] & external_marks[AVERAGE] & internal_marks[EXCELLENT], student_performance[GOOD])
    rule16 = ctrl.Rule(attendance[AVERAGE] & external_marks[AVERAGE] & internal_marks[AVERAGE], student_performance[AVERAGE])
    rule17 = ctrl.Rule(attendance[AVERAGE] & external_marks[POOR] & internal_marks[POOR], student_performance[POOR])
    rule18 = ctrl.Rule(attendance[AVERAGE] & external_marks[POOR] & internal_marks[GOOD], student_performance[AVERAGE])
    rule19 = ctrl.Rule(attendance[GOOD] & external_marks[AVERAGE] & internal_marks[AVERAGE], student_performance[AVERAGE])
    rule20 = ctrl.Rule(attendance[GOOD] & external_marks[EXCELLENT] & internal_marks[EXCELLENT], student_performance[VERY_GOOD])
    rule21 = ctrl.Rule(attendance[GOOD] & external_marks[GOOD] & internal_marks[AVERAGE], student_performance[GOOD])
    rule22 = ctrl.Rule(attendance[GOOD] & external_marks[POOR] & internal_marks[POOR], student_performance[POOR])
    rule23 = ctrl.Rule(attendance[VERY_GOOD] & external_marks[EXCELLENT] & internal_marks[VERY_GOOD], student_performance[VERY_GOOD])
    rule24 = ctrl.Rule(attendance[VERY_GOOD] & external_marks[VERY_GOOD] & internal_marks[VERY_GOOD], student_performance[VERY_GOOD])
    rule25 = ctrl.Rule(attendance[VERY_GOOD] & external_marks[POOR] & internal_marks[POOR], student_performance[POOR])
    rule26 = ctrl.Rule(attendance[VERY_GOOD] & external_marks[GOOD] & internal_marks[VERY_GOOD], student_performance[VERY_GOOD])
    rule27 = ctrl.Rule(attendance[VERY_GOOD] & external_marks[EXCELLENT] & internal_marks[EXCELLENT], student_performance[EXCELLENT])
    rule28 = ctrl.Rule(attendance[EXCELLENT] & external_marks[EXCELLENT] & internal_marks[VERY_GOOD], student_performance[VERY_GOOD])
    rule29 = ctrl.Rule(attendance[EXCELLENT] & external_marks[AVERAGE] & internal_marks[AVERAGE], student_performance[VERY_GOOD])
    rule30 = ctrl.Rule(attendance[EXCELLENT] & external_marks[AVERAGE] & internal_marks[VERY_GOOD], student_performance[GOOD])
    rule31 = ctrl.Rule(attendance[EXCELLENT] & external_marks[AVERAGE] & internal_marks[GOOD], student_performance[GOOD])
    rule32 = ctrl.Rule(attendance[EXCELLENT] & external_marks[POOR] & internal_marks[POOR], student_performance[POOR])
    rule33 = ctrl.Rule(attendance[EXCELLENT] & external_marks[AVERAGE] & internal_marks[POOR], student_performance[AVERAGE])
    rule34 = ctrl.Rule(attendance[EXCELLENT] & external_marks[POOR] & internal_marks[AVERAGE], student_performance[POOR])
    rule35 = ctrl.Rule(attendance[EXCELLENT] & external_marks[GOOD] & internal_marks[POOR], student_performance[GOOD])
    rule36 = ctrl.Rule(attendance[EXCELLENT] & external_marks[POOR] & internal_marks[GOOD], student_performance[AVERAGE])
    rule37 = ctrl.Rule(attendance[EXCELLENT] & external_marks[VERY_GOOD] & internal_marks[POOR], student_performance[VERY_GOOD])
    rule38 = ctrl.Rule(attendance[EXCELLENT] & external_marks[POOR] & internal_marks[VERY_GOOD], student_performance[AVERAGE])
    rule39 = ctrl.Rule(attendance[EXCELLENT] & external_marks[POOR] & internal_marks[EXCELLENT], student_performance[GOOD])
    rule40 = ctrl.Rule(attendance[EXCELLENT] & external_marks[AVERAGE] & internal_marks[EXCELLENT], student_performance[VERY_GOOD])
    rule41 = ctrl.Rule(attendance[EXCELLENT] & external_marks[GOOD] & internal_marks[EXCELLENT], student_performance[VERY_GOOD])
    rule42 = ctrl.Rule(attendance[EXCELLENT] & external_marks[VERY_GOOD] & internal_marks[EXCELLENT], student_performance[VERY_GOOD])
    rule43 = ctrl.Rule(attendance[EXCELLENT] & external_marks[EXCELLENT] & internal_marks[EXCELLENT], student_performance[EXCELLENT])

    # Creating a list of rules
    rule_list = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43]

    # Creating control system using the rules
    student_performance_ctrl = ctrl.ControlSystem(rule_list)

    # Creating simulation of the control system
    student_performance_analysis = ctrl.ControlSystemSimulation(student_performance_ctrl)

    # Setting the input values for the simulation
    student_performance_analysis.input[STUDENT_ATTENDANCE] = student_attendance
    student_performance_analysis.input[STUDENT_EXTERNAL_MARKS] = student_external_marks
    student_performance_analysis.input[STUDENT_INTERNAL_MARKS] = student_internal_marks

    # Running the simulation
    student_performance_analysis.compute()

    # Returning the output of the simulation as a string
    return str(student_performance_analysis.output[STUDENT_PERFORMANCE])

# Example usage of the function
# Printing the output obtained after running the code 
print(compute_student_performance(70, 20, 50))
print(compute_student_performance(90, 30, 60))
print(compute_student_performance(95, 90, 80))