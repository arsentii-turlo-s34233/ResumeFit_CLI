from ResumeFit.analyzer import analyze_documents

from ResumeFit.exceptions import EmptyFileError, DocumentsNotLoadedError

from ResumeFit.report import print_report

from ResumeFit.storage import load_txt_file, save_json_file

def run():
    resume_document = None
    job_document = None
    last_result = None

    running = True

    while running:
        print("")
        print("ResumeFit CLI")
        print("1. Load Resume")
        print("2. Load Job description")
        print("3. Show loaded status")
        print("4. Analyze resume fit")
        print("5. Export last result to JSON")
        print("0. Quit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            path = input("Enter resume path: ").strip()
            try:
                resume_document = load_txt_file(path)
                print("Resume loaded.")
            except FileNotFoundError:
                print("Error: Resume file not found.")
            except EmptyFileError:
                print("Error: Resume file is empty.")

        elif choice == "2":
            path = input("Enter job description path: ").strip()
            try:
                job_document = load_txt_file(path)
                print("Job description loaded.")
            except FileNotFoundError:
                print("Error: Job description file not found.")
            except EmptyFileError:
                print("Error: Job description file is empty.")

        elif choice == "3":
            print("Resume loaded: ", resume_document is not None)
            print("Job description loaded: ", job_document is not None)

        elif choice == "4":
            try:
                last_result = analyze_documents(resume_document, job_document)
                print_report(last_result)
            except DocumentsNotLoadedError as error:
                print("Error:", error)

        elif choice == "5":
            if last_result is None:
                print("No results found. Please run option 4 first.")
            else:
                save_json_file(last_result)

        elif choice == "0":
            print("Quitting...")
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice!")