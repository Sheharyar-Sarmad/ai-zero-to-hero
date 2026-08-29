

## Many To Many Relationship:

> A many-to-many relationship exists when multiple records in one table are associated with multiple records in another table.

## Simple Definition

> A many-to-many relationship means:

**ONE student can take MANY courses**
**ONE course can have MANY student**

## In a many-to-many relationship, you need THREE tables:

┌─────────────┐     ┌──────────────────┐     ┌─────────────┐
│  students   │     │   enrollments    │     │   courses   │
│             │     │  (Junction Table)│     │             │
│ student_id  │───▶  student_id        ◀───    course_id  
│ name        │     │ course_id        │     │ course_name │
│ age         │     │ enrollment_date  │     │ credits     │
└─────────────┘     └──────────────────┘     └─────────────┘

> The junction table contains the foreign keys from BOTH tables!

# Basic SQL Quiries To Implement **Juntion Table**

-- 1. Students table
**CREATE TABLE students (**
    **student_id SERIAL PRIMARY KEY,**
    **name VARCHAR(50) NOT NULL,**
    **age INTEGER**
**);**

-- 2. Courses table
**CREATE TABLE courses (**
    **course_id SERIAL PRIMARY KEY,**
    **course_name VARCHAR(100) NOT NULL,**
    **credits INTEGER**
**);**

-- 3. Junction table (Enrollments)
**CREATE TABLE enrollments (**
    **enrollment_id SERIAL PRIMARY KEY,**
    **student_id INTEGER REFERENCES students(student_id)**,
    **course_id INTEGER REFERENCES courses(course_id),**
    **enrollment_date DATE DEFAULT CURRENT_DATE,**
    **grade VARCHAR(2),**
    
    -- Prevent duplicate enrollments
    **UNIQUE(student_id, course_id)**
**);**