from flask import Flask, request, jsonify
from .utility import *
from .search_algo import *
app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from the url parameter /getmsg/?name=
    name = request.args.get("name", None)

    # For debugging
    print(f"Received: {name}")

    response = {}

    # Check if the user sent a name at all
    if not name:
        response["ERROR"] = "No name found. Please send a name."
    # Check if the user entered a number
    elif str(name).isdigit():
        response["ERROR"] = "The name can't be numeric. Please send a string."
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome API!"

    # Return the response in json format
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome API!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to rahul api center!</h1>"

@app.route('/binary-search', methods=['GET'])
def search_route():
    # Retrieve the name from the url parameter /getmsg/?name=
    values = request.args.get("values", None)
    key = request.args.get("key", None)

    response = {}
    res = None
    if not values and not key:
        return """
            <h1>Binary Search</h1>
            Binary Search is a searching algorithm for finding an element's position in a sorted array.<br>
            In this approach, the element is always searched in the middle of a portion of an array.<br><br>

            Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.<br>

            <h3>Binary Search Working</h3> <br>
            Binary Search Algorithm can be implemented in two ways which are discussed below.<br>

            <ul>
                <li>Iterative Method</li>
                <li>Recursive Method</li>
            </ul>
            The recursive method follows the divide and conquer approach.<br>

            The general steps for both methods are discussed below.<br>

            The array in which searching is to be performed is:<br>
            initial array Binary Search
            Initial array

            Let x = 4 be the element to be searched.<br>
            Set two pointers low and high at the lowest and the highest positions respectively.<br>
            setting pointers Binary Search
            Setting pointers<br>
            Find the middle element mid of the array ie. arr[(low + high)/2] = 6.<br>
            mid element Binary Search<br>
            Mid element<br>
            If x == mid, then return mid.Else, compare the element to be searched with m.<br>
            If x > mid, compare x with the middle element of the elements on the right side of mid. This is done by setting low to low = mid + 1.<br>
            Else, compare x with the middle element of the elements on the left side of mid. This is done by setting high to high = mid - 1.<br>
            finding mid element Binary Search<br>
            Finding mid element<br>
            Repeat steps 3 to 6 until low meets high.<br>
            mid element Binary Search<br>
            Mid element<br>
            x = 4 is found.<br>
        """

    # Check if the user sent a name at all
    if not values:
        response["ERROR"] = "Please provide input list"
    # Check if the user entered a number
    elif not key:
        response["ERROR"] = "Nothing to seach!! No key provided."
    else:
        values = list(map(int, values.split(',')))
        key = int(key)
        res = execution_time(binary_search, values=values, key=key)
        if res[0] == 0:
            response['ERROR'] = "Internal Server Error"
        else:
            response['SUCCESS'] = "KEY FOUND" if res[2] else "NOT FOUND"
            response["EXEC_TIME"] = res[1]
    
    # Return the response in json format
    return jsonify(response)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)