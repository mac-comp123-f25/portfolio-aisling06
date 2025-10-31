class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee.
        """
        self.gender = gender
        self.will_comment = will_comment
        self.comments_received = 0

    def set_commenter_status(self, comment_status):
        self.will_comment = comment_status

    def receive_sexist_comment(self):
        self.comments_received += 1

    def get_gender(self):
        return self.gender
    def get_commenter_status(self):
        return self.will_comment
    def get_comments_received(self):
        return self.comments_received

    def __str__(self):
        """
        Produces a printable string format for this employee.
        """
        return (self.gender
                + " (will comment: " + str(self.will_comment) + "): "
                + str(self.comments_received)
                + " sexist comments received")
    

