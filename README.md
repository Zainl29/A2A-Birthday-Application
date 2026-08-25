

#### Prerequisites

1. **uv:** The Python package management tool 
2. python 3.13+



#### 1. Install dependencies

Open a terminal to activate the virtual environment with: 

`uv venv`

`.venv/Scripts/activate`

This will create the `.venv` directory and install the required packages.



#### 2. Start server and run the remote agent

In the same terminal, run the server with the remote agent with:

`uv run main.py`



#### 3. Run the client agent

Open a second terminal and run the client agent with:

`uv run --active client.py`

The client will interact with the agent in the terminal output
