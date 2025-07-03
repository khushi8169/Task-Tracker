from planner_graph import planner

if __name__ == '__main__':
    print("🔁 Welcome to Smart Task Planner")
    while True:
        user_input = input("🧑‍💻 Enter your task/project request: ")
        output = planner.invoke({"input": user_input})
        print("\n📋 Response:", output)