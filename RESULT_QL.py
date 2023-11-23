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
        "-g RandomGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.7",
        "-g RandomGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g RandomGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.7",
        "-g RandomGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.1,alpha=0.4,gamma=0.7",
        "-g RandomGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g RandomGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.9",
        "-g RandomGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.7",
        "-g RandomGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g RandomGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.7",
        "-g RandomGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.1,alpha=0.4,gamma=0.7",
        "-g RandomGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g RandomGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.9",
        "-g RandomGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.7",
        "-g RandomGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g RandomGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.7",
        "-g RandomGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.1,alpha=0.4,gamma=0.7",
        "-g RandomGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g RandomGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.9",
        
        "-g DirectionalGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.7",
        "-g DirectionalGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g DirectionalGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.7",
        "-g DirectionalGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.1,alpha=0.4,gamma=0.7",
        "-g DirectionalGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g DirectionalGhost -x 2000 -n 2010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.9",
        "-g DirectionalGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.7",
        "-g DirectionalGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g DirectionalGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.7",
        "-g DirectionalGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.1,alpha=0.4,gamma=0.7",
        "-g DirectionalGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g DirectionalGhost -x 1000 -n 1010 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.9",
        "-g DirectionalGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.7",
        "-g DirectionalGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g DirectionalGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.7",
        "-g DirectionalGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.1,alpha=0.4,gamma=0.7",
        "-g DirectionalGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.2,gamma=0.9",
        "-g DirectionalGhost -x 50 -n 60 --frameTime 0 -a epsilon=0.05,alpha=0.4,gamma=0.9",
    ]

    result_matrix = []

    print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Learning Params", "Agent", "Number of Ghosts", "Ghost Type", "Wins", "Average Score", "Epsilon", "Alpha", "Gamma", "Iterations"))
    print("="*130)

    for experiment in experiments:
        command = "python pacman.py -p PacmanQAgent {}".format(experiment)
        output = run_command(command)
        result = parse_output(output)
        # Extracting hyperparameters and iterations
        epsilon = float(re.search(r"epsilon=(\d\.\d+)", experiment).group(1))
        alpha = float(re.search(r"alpha=(\d\.\d+)", experiment).group(1))
        gamma = float(re.search(r"gamma=(\d\.\d+)", experiment).group(1))
        iterations = int(re.search(r"-x (\d+)", experiment).group(1))

        result_matrix.append({
            'Wins': result['Wins'],
            'Average Score': result['Average Score'],
            'Epsilon': epsilon,
            'Alpha': alpha,
            'Gamma': gamma,
            'Iterations': iterations
        })

    for i, experiment in enumerate(experiments):
        agent = re.search(r"-p (\w+)", experiment).group(1)  # Extracting the agent name
        num_ghosts = int(re.search(r"-k (\d+)", experiment).group(1))
        ghost_type = re.search(r"-g (\w+)", experiment).group(1)
        wins = result_matrix[i]['Wins'] if i < len(result_matrix) else 0
        avg_score = result_matrix[i]['Average Score'] if i < len(result_matrix) else 0
        epsilon = result_matrix[i]['Epsilon'] if i < len(result_matrix) else 0
        alpha = result_matrix[i]['Alpha'] if i < len(result_matrix) else 0
        gamma = result_matrix[i]['Gamma'] if i < len(result_matrix) else 0
        iterations = result_matrix[i]['Iterations'] if i < len(result_matrix) else 0
        ghost_type = ghost_type + " " if ghost_type == "RandomGhost" else ghost_type
        learning_params = "{} -x {} -n {}".format(experiment, iterations, epsilon, alpha, gamma)
        print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            learning_params, agent, num_ghosts, ghost_type, wins, avg_score, epsilon, alpha, gamma))

if __name__ == "__main__":
    main()
