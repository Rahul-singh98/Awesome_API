import time

def execution_time(func, **kwargs):
    """
        Utility function to calculate execution time of 
        a function
    """
    start_time = time.process_time()
    try:
        res = func(**kwargs)
        end_time = time.process_time()
        return [1, end_time - start_time, res]
    except:
        return [0]
    
