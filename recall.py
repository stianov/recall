from termcolor import colored
import os, sys, random

pairs = []

# Read CSV-file
# TODO: Support RFC 4180 https://datatracker.ietf.org/doc/html/rfc4180

csv = open(sys.argv[1], "r")
for i in csv.readlines():
    pairs.append([i.split(",")[0],i.split(",")[1]]) 

match sys.argv[2]:
    case "test":
        success_attempts = 0
        failed_attempts = 0
        random.shuffle(pairs)
        for i in pairs:
            os.system('cls||clear')
            print(colored("Question:", "green", attrs=["bold"]), i[0])
            print(colored("Answer:", "yellow", attrs=["bold"]), end=" ")
            user_answer = input()
            print(colored("Answer:", "red", attrs=["bold"]), i[1])
            if input("y/n: ") == "y":
                success_attempts += 1
            else:
                failed_attempts += 1
        os.system('cls||clear')
        print(colored("Results:", attrs=["bold"]))
        print(colored(str(success_attempts), "green"), " correct answers and ", colored(str(failed_attempts), "red"), " incorrect answers.")
    case "view":
        longest = 0
        for i in pairs:
            if(len(i[0]) > longest):
                longest = len(i[0])
        string = colored("Question", "green", attrs=["bold"])
        for x in range(longest - len("Question")):
             string += " "
        print(string, "| ", colored("Answer", "red", attrs=["bold"]))
        string = ""
        for x in range(longest + len(" | Answer ")):
            string += "-"
        print(string)
        for i in pairs:
            string = i[0]
            if len(string) < longest:
                for x in range(longest - len(string)):
                    string += " "
            print(string, "| ", i[1], end="")
    case default:
        print("No action.")
