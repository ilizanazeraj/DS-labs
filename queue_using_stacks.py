# code reference : https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
#                  https://www.geeksforgeeks.org/queue-using-stacks/

import logging

# Configure the logger
logging.basicConfig(level=logging.INFO) 

# Create a logger instance
logger = logging.getLogger(__name__)

class Stack:
    """Class Stack
    """    

    def __init__(self):
        """Initializer for Stack class
        """        
        self.elements = []

    def size(self):
        """ Returns the size of the Stack

        Returns:
            int: size of the stack
        """        
        return len(self.elements)

    def is_empty(self):
        """Checks if the stack is empty

        Returns:
            bool: Returns true/false if the stack is empty
        """        
        return len(self.elements) == 0

    def push(self, element):
        """Adds an element to the stack

        Args:
            element (string): element to be added to stack
        """        
        self.elements.append(element)

    def pop(self):
        """Deletes an element from Stack

        Returns:
            string: The element to be deleted
        """        
        if self.is_empty():
         
            logger.error("Stack is empty!")
        else:
            return self.elements.pop()


class Queue:
    """
    Class Queue
    """
    def __init__(self):
        """Queue initializer
        """        
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isEmpty(self):
        """Checks if the Queue is empty

        Returns:
            Bool: Returns true or false if the queue is empty
        """        
        result = self.stack1.is_empty() and self.stack2.is_empty()
        return result

    def size(self):
        """Returns the size of the queue

        Returns:
            int: Size of the queue
        """        
        return self.stack1.size() + self.stack2.size()

    def enQueue(self, element):
        """Adds an element to the Queue

        Args:
            element (string): Element to be added

        Returns:
            string: Element added
        """        
        # Add the element to stack 1
        self.stack1.push(element)
        return self.stack1.elements

    def deQueue(self):
        """Deletes an element from the Queue

        Returns:
            string: Element deleted
        """        
        if not self.isEmpty():
            # get the element from stack 1 and put them to stack 2 and return the element
            if self.stack2.is_empty():
                while self.stack1.size() > 0:
                    self.stack2.push(self.stack1.pop())
            return self.stack2.elements.pop()
        else:
            logger.error('The Queue is empty, cannot delete')

    def printQueue(self):
        """Prints the queue elements
        """        
        print("The queue elements are:", self.stack1.elements+self.stack2.elements)

def isBalanced(sequence):
    """Checks if a string is with balanced parenthesis

    Args:
        sequence (string): string to be checked

    Returns:
        bool: True if a string has balanced parathesis, otherwise false
    """    
    stack = Stack()
    openParenthesis=["(", "{", "["]
    for item in sequence:
        # add the opening parenthesis
        if item in openParenthesis:
            stack.push(item)
        else:
            if stack.is_empty():
                logger.info('Parenthesis are not balanced')
                return False
            # get the last item inserted in stack anf check if they match the closing
            current = stack.pop()
            # Check if it is closing
            if current == '(':
                if item != ")":
                    logger.info('Parenthesis are not balanced')
                    return False
            if current == '{':
                if item != "}":
                    logger.info('Parenthesis are not balanced')
                    return False
            if current == '[':
                if item != "]":
                    logger.info('Parenthesis are not balanced')
                    return False
                
    result= stack.is_empty()
    if result:
        logger.info('Parenthesis are balanced ')
    else:
        logger.info('Parenthesis are not balanced')

    return result
