import heapq

class Solution:
    def busiestServers(self, k: int, arrivals: List[int], loads: List[int]) -> List[int]:
        requests_handled = [0] * k
        
        available_servers = [i for i in range(k)]

        unavailable_servers = []

        for i in range(len(arrivals)):
            arrival = arrivals[i]
            load = loads[i]

            while unavailable_servers and unavailable_servers[0][0] <= arrival:
                _, server = heapq.heappop(unavailable_servers)
                server = server % k    
                heapq.heappush(available_servers, (i // k + (1 if i % k > server else 0)) * k + server)

            if not available_servers:
                continue

            server = heapq.heappop(available_servers) % k
            heapq.heappush(unavailable_servers, (arrival + load, server))
            requests_handled[server] += 1

        max_handled = max(requests_handled)    
        
        return [i for i in range(k) if requests_handled[i] == max_handled]
