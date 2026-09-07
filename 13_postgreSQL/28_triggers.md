

# Triggers : 

> Triggers are special procedures in a database that automatically execute predefined actions in response to certain events on a specified table or view.

# Syntax : 

<!-- 
CREATE TRIGGER trigger_name
{ BEFORE | AFTER | INSTEAD OF } { INSERT | UPDATE | DELETE | TRUNCATE }
ON table_name
FOR EACH { ROW | STATEMENT }
EXECUTE FUNCTION trigger_function_name();
 -->

# Example With Function : 

<!-- 
CREATE OR REPLACE FUNCTION check_salary()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salary < 0 THEN
        NEW.salary = 0;
    END IF;
    RETURN NEW;              
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_update_salary
BEFORE UPDATE ON employees
FOR EACH ROW 
EXECUTE FUNCTION check_salary();
 -->