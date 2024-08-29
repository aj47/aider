import sys
import urllib.parse
import webbrowser


def report_github_issue(issue_text, title=None):
    """
    Compose a URL to open a new GitHub issue with the given text prefilled,
    and attempt to launch it in the default web browser.

    :param issue_text: The text of the issue to file
    :param title: The title of the issue (optional)
    :return: None
    """
    base_url = "https://github.com/paul-gauthier/aider/issues/new"
    params = {"body": issue_text}
    if title is None:
        title = "Bug report"
    params["title"] = title
    issue_url = f"{base_url}?{urllib.parse.urlencode(params)}"

    try:
        print("Attempting to open the issue URL in your default web browser...")
        if webbrowser.open(issue_url):
            print("Browser window should be opened.")
        else:
            print("Unable to open browser window automatically.")
    except Exception as e:
        print()
        print("Please use this URL to file a GitHub issue:")
        print()
        print(issue_url)



if __name__ == "__main__":
    title = None
    if len(sys.argv) > 2:
        # Use the first command-line argument as the title and the second as the issue text
        title = sys.argv[1]
        issue_text = sys.argv[2]
    elif len(sys.argv) > 1:
        # Use the first command-line argument as the issue text
        issue_text = sys.argv[1]
    else:
        # Read from stdin if no argument is provided
        print("Enter the issue title (optional, press Enter to skip):")
        title = input().strip()
        if not title:
            title = None
        print("Enter the issue text (Ctrl+D to finish):")
        issue_text = sys.stdin.read().strip()

    report_github_issue(issue_text, title)
