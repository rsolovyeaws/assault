from typing import List, Dict
from statistics import mean

class Results:
    """ Results handles calculating statistics based on a list of requests that were made.
    Here's example of what the information will look like:
    
    Successful requests     500 
    Slowest                 0.010s 
    Fastest                 0.001s 
    Average                 0.003s 
    Total time              0.620s 
    Requests Per Minute     48360 
    Requests Per Second     806 
    """
    
    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = sorted(requests, key=lambda r: r["request_time"])
    
    def slowest(self) -> float:
        """
        Returns the slowest request completion time.
        
        >>> results = Results(10.6, [{
        ...     "status_code": 200,
        ...     "request_time": 3.4,
        ... }, {
        ...     "status_code": 500,
        ...     "request_time": 6.1,
        ... }, {
        ...     "status_code": 200,
        ...     "request_time": 1.04,
        ... }])
        >>> results.slowest()
        6.1
        """
        return self.requests[-1]["request_time"]
    
    def fastest(self) -> float:
        """
        Returns the fastest request completion time.
        
        >>> results = Results(10.6, [{
        ...     "status_code": 200,
        ...     "request_time": 3.4,
        ... }, {
        ...     "status_code": 500,
        ...     "request_time": 6.1,
        ... }, {
        ...     "status_code": 200,
        ...     "request_time": 1.04,
        ... }])
        >>> results.fastest()
        1.04
        """
        return self.requests[0]["request_time"]
    
    def average_time(self) -> float:
        """
        Returns the average request completion time.
        
        >>> results = Results(10.6, [{
        ...     "status_code": 200,
        ...     "request_time": 3.4,
        ... }, {
        ...     "status_code": 500,
        ...     "request_time": 6.1,
        ... }, {
        ...     "status_code": 200,
        ...     "request_time": 1.04,
        ... }])
        >>> results.average_time()
        3.513333333333333
        """
        return mean([r["request_time"] for r in self.requests])

    def requests_per_minute(self) -> int:
        """
        Returns the number of requests that could be made in a minute.
        
        >>> results = Results(10.6, [{
        ...     "status_code": 200,
        ...     "request_time": 3.4,
        ... }, {
        ...     "status_code": 500,
        ...     "request_time": 6.1,
        ... }, {
        ...     "status_code": 200,
        ...     "request_time": 1.04,
        ... }])
        >>> results.requests_per_minute()
        17
        """
        return round(60 * len(self.requests) / self.total_time)
    
    def requests_per_second(self) -> int:
        """
        Requests the number of requests made per second.
        
        >>> results = Results(3.5, [{
        ...     "status_code": 200,
        ...     "request_time": 3.4,
        ... }, {
        ...     "status_code": 500,
        ...     "request_time": 2.9,
        ... }, {
        ...     "status_code": 200,
        ...     "request_time": 1.04,
        ... }, {
        ...     "status_code": 200,
        ...     "request_time": 0.4,
        ... }])
        >>> results.requests_per_second()
        1
        """
        return round(len(self.requests) / self.total_time)
    
    def successfull_requests(self) -> int:
        """
        Returns the slowest request completion time.
        
        >>> results = Results(10.6, [{
        ...     "status_code": 200,
        ...     "request_time": 3.4,
        ... }, {
        ...     "status_code": 500,
        ...     "request_time": 6.1,
        ... }, {
        ...     "status_code": 200,
        ...     "request_time": 1.04,
        ... }])
        >>> results.successfull_requests()
        2
        """
        return len([r for r in self.requests if r["status_code"] in range(200, 299)])