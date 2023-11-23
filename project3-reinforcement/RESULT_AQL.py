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
        "-g RandomGhost -p ApproximateQAgent -a extractor=IdentityExtractor -x 50 -n 60 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=IdentityExtractor -x 100 -n 110 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=IdentityExtractor -x 200 -n 210 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=CoordinateExtractor -x 50 -n 60 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=CoordinateExtractor -x 100 -n 110 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=CoordinateExtractor -x 200 -n 210 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=SimpleExtractor -x 100 -n 110 -l mediumClassic --frameTime 0",
        "-g RandomGhost -p ApproximateQAgent -a extractor=SimpleExtractor -x 200 -n 210 -l mediumClassic --frameTime 0",

        "-g DirectionalGhost -p ApproximateQAgent -a extractor=IdentityExtractor -x 50 -n 60 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=IdentityExtractor -x 100 -n 110 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=IdentityExtractor -x 200 -n 210 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=CoordinateExtractor -x 50 -n 60 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=CoordinateExtractor -x 100 -n 110 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=CoordinateExtractor -x 200 -n 210 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=SimpleExtractor -x 100 -n 110 -l mediumClassic --frameTime 0",
        "-g DirectionalGhost -p ApproximateQAgent -a extractor=SimpleExtractor -x 200 -n 210 -l mediumClassic --frameTime 0",
    ]

    result_matrix = []

    print("{:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Extractor Type", "Learning Params", "Agent", "Wins", "Average Score", "Iterations", "Extractor"))
    print("="*115)

    for experiment in experiments:
        command = "python pacman.py {}".format(experiment)
        output = run_command(command)
        result = parse_output(output)
        # Extracting hyperparameters and iterations
        extractor_type = re.search(r"-a extractor=(\w+)", experiment).group(1)
        iterations = int(re.search(r"-x (\d+)", experiment).group(1))

        result_matrix.append({
            'Wins': result['Wins'],
            'Average Score': result['Average Score'],
            'Iterations': iterations,
            'Extractor Type': extractor_type
        })

    for i, experiment in enumerate(experiments):
        agent = re.search(r"-p (\w+)", experiment).group(1)  # Extracting the agent name
        wins = result_matrix[i]['Wins'] if i < len(result_matrix) else 0
        avg_score = result_matrix[i]['Average Score'] if i < len(result_matrix) else 0
        iterations = result_matrix[i]['Iterations'] if i < len(result_matrix) else 0
        extractor_type = result_matrix[i]['Extractor Type'] if i < len(result_matrix) else 0
        print("{:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            extractor_type, experiment, agent, wins, avg_score, iterations, extractor_type))

if __name__ == "__main__":
    main()
