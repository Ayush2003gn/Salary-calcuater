START

DISPLAY "Employee Database"

INPUT emp_id

FETCH all employees from database

IF emp_id is found THEN
    DISPLAY employee_name
    DISPLAY basic_salary

    HRA ← 0.15 × basic_salary
    DA  ← 0.10 × basic_salary
    TA  ← 0.20 × basic_salary

    gross_salary ← basic_salary + HRA + DA + TA

    DISPLAY HRA, DA, TA
    DISPLAY gross_salary
ELSE
    DISPLAY "ID not found"
END IF

STOP
