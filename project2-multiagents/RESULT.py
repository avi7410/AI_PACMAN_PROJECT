import subprocess
import re

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output

def parse_output(output):
    scores = re.findall(r"Score: (\d+)", output)
    wins = re.findall(r"Win", output)
    average_score = sum(map(float, scores)) / len(scores) if scores else 0
    return {
        'Wins': len(wins),
        'Average Score': average_score,
        'Scores': map(float, scores),
    }

def main():
    experiments = [
        "--frameTime 0 -p LeftTurnAgent -k 2 -n 10 -g RandomGhost",
        "--frameTime 0 -p LeftTurnAgent -k 2 -n 10 -g DirectionalGhost",
        "--frameTime 0 -p GreedyAgent -k 2 -n 10 -g RandomGhost",
        "--frameTime 0 -p GreedyAgent -k 2 -n 10 -g DirectionalGhost",
        "--frameTime 0 -p ReflexAgent -k 2 -n 10 -g RandomGhost",
        "--frameTime 0 -p ReflexAgent -k 2 -n 10 -g DirectionalGhost",
        "--frameTime 0 -p MinimaxAgent -k 2 -n 10 -g RandomGhost -a depth=3",
        "--frameTime 0 -p MinimaxAgent -k 2 -n 10 -g DirectionalGhost -a depth=3",
        "--frameTime 0 -p AlphaBetaAgent -k 2 -n 10 -g RandomGhost -a depth=3",
        "--frameTime 0 -p AlphaBetaAgent -k 2 -n 10 -g DirectionalGhost -a depth=3",
        "--frameTime 0 -p ExpectimaxAgent -k 2 -n 10 -g RandomGhost -a depth=3",
        "--frameTime 0 -p ExpectimaxAgent -k 2 -n 10 -g DirectionalGhost -a depth=3",
        "--frameTime 0 -p LeftTurnAgent -k 1 -n 10 -g RandomGhost",
        "--frameTime 0 -p LeftTurnAgent -k 1 -n 10 -g DirectionalGhost",
        "--frameTime 0 -p GreedyAgent -k 1 -n 10 -g RandomGhost",
        "--frameTime 0 -p GreedyAgent -k 1 -n 10 -g DirectionalGhost",
        "--frameTime 0 -p ReflexAgent -k 1 -n 10 -g RandomGhost",
        "--frameTime 0 -p ReflexAgent -k 1 -n 10 -g DirectionalGhost",
        "--frameTime 0 -p MinimaxAgent -k 1 -n 10 -g RandomGhost -a depth=3",
        "--frameTime 0 -p MinimaxAgent -k 1 -n 10 -g DirectionalGhost -a depth=3",
        "--frameTime 0 -p AlphaBetaAgent -k 1 -n 10 -g RandomGhost -a depth=3",
        "--frameTime 0 -p AlphaBetaAgent -k 1 -n 10 -g DirectionalGhost -a depth=3",
        "--frameTime 0 -p ExpectimaxAgent -k 1 -n 10 -g RandomGhost -a depth=3",
        "--frameTime 0 -p ExpectimaxAgent -k 1 -n 10 -g DirectionalGhost -a depth=3",
    ]

    result_matrix = []

    print("{:<20} {:<15} {:<15} {:<15} {:<15}".format(
        "Agent", "Number of Ghosts", "Ghost Type", "Wins", "Average Score"))
    print("="*80)

    for experiment in experiments:
        command = "python pacman.py {}".format(experiment)
        output = run_command(command)
        result = parse_output(output)
        result_matrix.append(result)

    for i, experiment in enumerate(experiments):
        agent = re.search(r"-p (\w+)", experiment).group(1)  # Extracting the agent name
        num_ghosts = int(re.search(r"-k (\d+)", experiment).group(1))
        ghost_type = re.search(r"-g (\w+)", experiment).group(1)
        wins = result_matrix[i]['Wins'] if i < len(result_matrix) else 0
        avg_score = result_matrix[i]['Average Score'] if i < len(result_matrix) else 0
        ghost_type = ghost_type + " " if ghost_type == "RandomGhost" else ghost_type
        print("{:<20} {:<15} {:<15} {:<15} {:<15}".format(
            agent, num_ghosts, ghost_type, wins, avg_score))

if __name__ == "__main__":
    main()
