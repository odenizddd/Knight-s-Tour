import sys
import LasVegas, Backtracking

part = None

try:
    part = sys.argv[1]
except IndexError:
    print("\033[31mPlease provide enough arguments.\033[0m")

# Define board size
n = 8

if part == "part1":
    # Define a list of success threshold to conduct the experiment with.
    success_threshold_list = [0.7, 0.8, 0.85]
    for success_threshold in success_threshold_list:
    # Clear the output file
        with open(f"results_{success_threshold}.txt", "w") as file:
            pass
        # Run the actual simulation
        number_of_runs = 100000
        successful_runs = 0
        for i in range(number_of_runs):
            if LasVegas.run(n, success_threshold, i+1):
                successful_runs += 1
        print(f"LasVegas Algorithm With p = {success_threshold}")
        print(f"Number of successful tours: {successful_runs}")
        print(f"Number of trials: {number_of_runs}")
        print(f"Probability of a successful tour: {successful_runs/number_of_runs}")

if part == "part2":
    # Number of trials for each experiment
    run_count = 100000

    # p and k are defined in the description
    p_list = [0.7, 0.8, 0.85]
    k_list = [0, 2, 3]

    args = [(n, run_count, p, k) for p in p_list for k in k_list]

    for arg in args:
        Backtracking.run(arg)