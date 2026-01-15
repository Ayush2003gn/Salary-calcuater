DEFINE function database()
    STORE employees as list of tuples
    RETURN employees
END FUNCTION

DEFINE function salary(x)
    hra ← 0.15 × x
    da  ← 0.10 × x
    ta  ← 0.202 × x
    gross ← x + hra + da + ta

    PRINT hra, da, ta
    PRINT gross
END FUNCTION


INPUT employee_id

TRY
    employee_id ← INTEGER(employee_id)
CATCH error
    employee_id ← NONE
END TRY


FOR each emp IN database()

    IF emp.id = employee_id THEN
        PRINT emp.name, emp.basic_salary
        CALL salary(emp.basic_salary)
        STOP LOOP
    END IF

END FOR


IF employee_id = NONE THEN
    PRINT "ID not found"
ELSE IF employee_id > 5 THEN
    PRINT "No Input"
END IF