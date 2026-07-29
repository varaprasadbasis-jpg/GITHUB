from flask import Flask, jsonify

app = Flask(__name__)
votes = {}
@app.route('/vote/<candidate_name>', methods=['GET'])
def vote_for_candidate(candidate_name):
    if candidate_name in votes:
        votes[candidate_name] += 1
    else:
        votes[candidate_name] = 1
        
    return jsonify({
        'message': f'Vote recorded for {candidate_name}',
        'current_votes': votes[candidate_name],
        'all_votes': votes
    }), 200

@app.route('/votes', methods=['GET'])
def get_votes():
    return jsonify({'all_votes': votes}), 200

@app.route('/reset', methods=['GET'])
def reset_votes():
    votes.clear()  # Clears the dictionary holding the vote counts
    return jsonify({"message": "All votes have been reset successfully", "votes": votes}), 200

if __name__ == '__main__':
    app.run(debug=True)