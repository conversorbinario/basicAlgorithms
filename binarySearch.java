package learning;

import java.util.Scanner;



/* BINARY SEARCH, BUBBLE ALGORITHM and LINEAR SEARCH ALGORITHM
 This is a simple but somewhat long program whose aim is to show, for begginners,
 how these three simple, popular algorithms work.
 Binary Search Algortihm (BSA) allows you to SEARCH elements in an ordered list efficiently.
 Bubble Algorithm allows you to SORT element in a list. This is a previous step
 needed to use the BSA.
 Linear Search Algorithm is a more intuitive way of SEARCHING an element in a list.
 We use it so you can see how it works and you can compare its lower efficiency against 
 the BSA
    */
public class binarySearch {
	public static void main(String[] args) {

		/*
		 * There a few things you do not really need to understand, but that are
		 * included in this simple program. My advice is not to spend time trying to
		 * completely understand them. There is enough information in the comments so
		 * you can grasp the basics needed. Don't lose sight of understanding the main
		 * idea of the algorithm, which is main the goal. Things you don't need to know about, but that
		 * are used 1.What's a matrix in Java and how it works 2.How to use imported
		 * Classes in Java. 3. How to implement (code) the Bubble Sort Algorithm (but it
		 * is interesting to see how it works, to have an idea of what a Brute Force
		 * Algorithm does; there's a short explanation in the comments.)
		 * Finally I've included a Linear Search Algorithm. This algorithm is very simple. 
		 * I am counting the number of steps you would be doing to perform the same searching operation
		 * in a linear way (comparing each element to the searching term) instead of with the Binary Search.
		 * This illustrates the main point of using the Binary Search Algorithm: finding information in less steps;
		 * being more efficient. More information about this point in the Binary Search part.
		 * 
		 */

		String[] names = new String[10]; /*  This is called matrix. A matrix can store lists. It will store the list
											 * of names where we'll search a given name. The number indicated between [
											 * ] indicates the number of values we are going to store in it. It is not
											 * important now; just keep in mind that we will store the values we want to
											 * use in it
											 */
		int[] numbers = new int[10]; /* Same here, but we will store integer numbers in this list */
		int answer;
		Scanner teclado = new java.util.Scanner(System.in);

		System.out.println("Introduce number 1 for searching a value in a list of NUMBERS "
				+ "\nNumber  0 for searching a value in a list of NAMES");

		answer = teclado.nextInt();

		while (!(answer == 0 || answer == 1)) { // In case you don't introduce number 1 or number 0, the program
												// asks for a number again
			System.out.println("Introduce number 1 for searching a value in a list of NUMBERS");
			System.out.println("\nNumber  0 for searching a value in a list of NAMES");

			answer = teclado.nextInt();
		}

		// INPUT PART. Either names or numbers.

		if (answer == 0) {
			System.out.println("Now, introduce the names:");
			/* Here we are just introducing the names */
			int i;

			for (i = 0; i < names.length; i++) { /*
													 * Condition to stop the loop is that i is smaller than the number
													 * of items in our list. This allows us to introduce as many names
													 * (no more no less) as we stated for our matrix
													 */
				names[i] = teclado.nextLine();

			}
		}

		else {
			System.out.println("Now, introduce the numbers:");
			for (int i = 0; i < names.length; i++) {
				numbers[i] = teclado.nextInt();
			}
		}

		/*
		 * At this point, we've already introduced our ten names OR numbers. But, as you
		 * might recall in order to apply our binary search algorithm, **we must
		 * sort(beforehand)** the names alphabetically (names) or in an increasing
		 * manner (numbers)
		 */

		/*
		 * Now we are going to sort the list in alphabetical (names) or from the
		 * smallest to the largest (numbers) This a necessary PREVIOUS step in order to
		 * apply the binary search algorithm. There are methods in Java that can do
		 * this: you just need to import java.util.Arrays; then write
		 * Arrays.sort(array_Iam_sorting); and there you go). However, we'll do it
		 * manually using a Brute Force Algorithm -an algorithm that iterates over all
		 * the items to sort them-
		 */

		/*
		 * The algorithm we'll use is pretty popular, and it is called Bubble Sort
		 * Algorithm. In this algorithm, we have a list of numbers we want to sort.
		 * Between [ and ], the pairs we are going to compare in each iteration. Then,
		 * step by step, we compare each pair of numbers, starting with the first and
		 * the second. For instance: List: [9, 5],1, 8. (9 vs. 5) If the first numbers
		 * of the pair is larger: we move it forward. (Our list now: 5, 9, 1, 8) if it
		 * is not: we do nothing. Then we compare the second number of *our pair* to
		 * the next one in the list. List: 5, [9, 1], 8 (so we compare *9*, 2nd number
		 * of our pair, to 1) (9 vs 1.). If it is larger, we move it forward. (list
		 * now: 5, 1, 9, 8). Otherwise, we do nothing. We repeat this process. List with
		 * the next comparison: 5, 1, [9, 8]. 1.Compare 2.Move if necessary. Final
		 * result of the first ordering sequence: 5, 1, 8, 9.
		 * 
		 * Once we have arrived to the last comparison (9 vs 8, in this case), we start
		 * the same process again (until the number "Last comparison-1",
		 * "last comparison -2") and so on, in each iteration.
		 * 
		 * This is because there's no need of comparing the last number- we already know
		 * that it is the largest. So we would "forget" about number 9, and just do the
		 * process through: 5, 1 and 8 (last comparison: 1 vs 8).
		 */

		/****** SORTING PART. */

		// SORTING PART FOR NUMBERS
		if (answer == 1) {
			int limit_iteration = numbers.length - 1; // Number 9th in our ten list
			int smallerNumber;

			int completeIterationsNumber = numbers.length - 1;

			while (completeIterationsNumber > 1) {
				for (int i = 0; i < limit_iteration; i++) { /*
															 * so limit is i < 9, this means UNTIL i=8, i=7 in the next
															 * loop, etc. We do this because we are comparing to
															 * i+1 if i=9, i+1=10 which is out of the matrix
															 */
					if (numbers[i] > numbers[i + 1]) { //
						smallerNumber = numbers[i + 1];
						numbers[i + 1] = numbers[i];
						numbers[i] = smallerNumber;
					}

					if (i == limit_iteration
							- 1) { /*
									 * This makes that, once we are in the last number (8th, then 7, 6, 5 and so on
									 * in the next ones), the limit for the next phase is our current limit less one
									 * (this is how we get 7, 6, etc). This is explained more thoroughly above.
									 */
						limit_iteration = limit_iteration - 1;

					}

				}

				completeIterationsNumber--;
			}

			// JUST PRINTING ORDERED NUMBERS.

			for (int i = 0; i < numbers.length; i++) {

				System.out.println(numbers[i]);
			}

		}

		/*
		 * SORTNG PART FOR NAMES With names, we use the same Algorithm. We just use soe
		 * different methods, given the fact that we are using Strings and not numbers.
		 */

		else {
			int limit_iterationName = names.length - 1;
			int completeIterationsNames = names.length - 1;
			String backwardsWord;

			while (completeIterationsNames > 1) {
				for (int i = 0; i < limit_iterationName; i++) { // so limit is i < 9, this means UNTIL i=8, i=7 in the
																// next
					// loop, etc

					if (names[i].compareToIgnoreCase(names[i + 1]) > 0) { //
						backwardsWord = names[i + 1];
						names[i + 1] = names[i];
						names[i] = backwardsWord;
					}

					if (i == limit_iterationName - 1) {

						limit_iterationName = limit_iterationName - 1;

					}

				}

				completeIterationsNames--;

			}

			//Just PRINTING SORTED NAMES.
			for (int i = 0; i < names.length; i++) {

				System.out.println(names[i]);
			}

		}

		/***** SEARCHING PART. */
		// SEARCHING PART FOR NAMES
		String searchName = ""; /*
								 * We'll assign a value to these variables with the keyboard, initializing them here so the
								 * compiler doesn't find any trouble now
								 */
		int searchNumber = 0;

		if (answer == 0) {
			int lowest = 0;
			boolean found = false;
			int highest = names.length - 1;
			int numberOfIterations = 0;
			int currentComparison = (lowest + highest) / 2;

			System.out.println("Introduce the name you are looking for");
			searchName = teclado.nextLine();

			while (lowest <= highest) {
				numberOfIterations++; /* Just a counter that shows you how many steps you have
										We'll use it to compare the number steps in BSA vs Linear Search Algorithm.*/
				currentComparison = (lowest + highest) / 2;
				if (searchName.compareToIgnoreCase(names[currentComparison]) == 0) {
					found = true;
					break; //if we find it, we stop the while - that's what the break does
				} else if (searchName.compareToIgnoreCase(names[currentComparison]) < 0) {
					highest = currentComparison - 1;
				} else {
					lowest = currentComparison + 1;
				}

			}

			if (found) {
				System.out.println("Yes, there is a person called: " + names[currentComparison] + " in the list");
			} else {
				System.out.println("There's nobody called: " + searchName);
			}

			System.out.println("Number of steps you have performed with the Binary Search Algorithm: " + numberOfIterations);
			
			
			
			// THIS PART PEFORMS A LINEAR SEARCH ALGORITHM. I just put it aside so you don't mix it with the other parts.
		
			int iterationsFor = 0;
			for (int i = 0; i < names.length; i++) {
				iterationsFor = i + 1;
				if (searchName == names[i]) {
					break;
				}
			}
			System.out.println("Number of steps you have performed comparing the searching term with each word: " + iterationsFor);
		}

			
		

		else {

			int lowest = 0;
			boolean found = false;
			int highest = numbers.length - 1;
			int numberOfIterations = 0;
			int currentComparison = (lowest + highest) / 2;

			System.out.println("Introduce the number you are looking for");
			searchNumber = teclado.nextInt();

			while (lowest <= highest) {
				numberOfIterations++; // Not necessary, just a counter that shows you how many steps you have
										// performed
				currentComparison = (lowest + highest) / 2;
				if (searchNumber == numbers[currentComparison]) {
					found = true;
					break; 
				} else if (searchNumber < numbers[currentComparison]) {
					highest = currentComparison - 1;
				} else {
					lowest = currentComparison + 1;
				}

			}

			if (found) {
				System.out.println("Yes, number: " + numbers[currentComparison] + " appears in the list");
			} else {
				System.out.println("NUmber: " + searchNumber + " doesn't appear in the list");
			}

			System.out.println("Number of steps you have performed with the Binary Search Algorithm: " + numberOfIterations);

			
			
			// LINEAR SEARCH ALGORITHM for numbers. 
			int iterationsFor = 0;
			int i;

			for (i = 0; i < numbers.length; i++) {
				iterationsFor = i + 1;
				if (searchNumber == numbers[i]) {
					break;
				}
			}

			System.out.println("Number of steps you have performed comparing the searching term with the searching number: " + iterationsFor);

		}

		teclado.close();

	}

}
