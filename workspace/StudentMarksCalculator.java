/**
 * DevPulse AI - Student Marks & Grade Calculator
 * Language: Java
 */
import java.util.Scanner;

public class StudentMarksCalculator {
    public static void main(String[] args) {
        System.out.println("==========================================");
        System.out.println("🎓 Student Marks & Grade Calculation System");
        System.out.println("==========================================");

        String[] subjects = {"Mathematics", "Computer Science", "Physics", "English", "Chemistry"};
        int[] marks = {92, 98, 88, 85, 90}; // Sample benchmark grades
        
        int totalMarks = 0;
        int maxMarks = subjects.length * 100;

        System.out.println("
Subject Breakdown:");
        for (int i = 0; i < subjects.length; i++) {
            System.out.printf("  • %-18s: %3d / 100
", subjects[i], marks[i]);
            totalMarks += marks[i];
        }

        double percentage = ((double) totalMarks / maxMarks) * 100.0;
        String grade;
        
        if (percentage >= 90.0) grade = "A+ (Outstanding)";
        else if (percentage >= 80.0) grade = "A (Excellent)";
        else if (percentage >= 70.0) grade = "B (Good)";
        else if (percentage >= 60.0) grade = "C (Satisfactory)";
        else grade = "F (Needs Improvement)";

        System.out.println("
------------------------------------------");
        System.out.printf("Total Score : %d / %d
", totalMarks, maxMarks);
        System.out.printf("Percentage  : %.2f%%
", percentage);
        System.out.printf("Final Grade : %s
", grade);
        System.out.println("==========================================");
    }
}
