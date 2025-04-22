from experta import *

class HelpDeskSystem(KnowledgeEngine):
    
    @DefFacts()
    def _initial_action(self):
        print("🤖 Welcome to Help Desk Expert System!")
        print("Tell me your issue... (e.g., 'internet', 'password', 'printer')")
        yield Fact(action='helpdesk')

    # Rule for internet issue
    @Rule(Fact(action='helpdesk'), Fact(issue='internet'))
    def internet_issue(self):
        print("🔧 Tip: Try restarting your router. If it doesn't work, check your network settings.")

    # Rule for password issue
    @Rule(Fact(action='helpdesk'), Fact(issue='password'))
    def password_issue(self):
        print("🔐 Tip: You can reset your password from the login page by clicking 'Forgot Password'.")

    # Rule for printer issue
    @Rule(Fact(action='helpdesk'), Fact(issue='printer'))
    def printer_issue(self):
        print("🖨️ Tip: Check if the printer is turned on and connected. Also check for paper or ink errors.")

    # Rule for unknown issue
    @Rule(Fact(action='helpdesk'), NOT(Fact(issue=W())))
    def unknown_issue(self):
        print("❓ I'm not sure about that issue. Please contact a human technician.")

# Run the expert system
engine = HelpDeskSystem()
engine.reset()

user_input = input("Enter your issue keyword: ").lower()
engine.declare(Fact(issue=user_input))
engine.run()
