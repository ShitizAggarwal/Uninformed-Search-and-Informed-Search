class PriorityQueue:
    k_v = {}
    v_k = {}
    P_Keys = []

    def put(self, pq_key, pq_value):
        if pq_value in list(self.v_k.keys()):
            od_k = self.v_k[pq_value]
            self.v_k[pq_value] = pq_key
            self.k_v[pq_key] = pq_value
            self.P_Keys[self.P_Keys.index(od_k)] = pq_key
            self.P_Keys.sort()
        else:
            self.k_v[pq_key] = pq_value
            self.v_k[pq_value] = pq_key
            self.P_Keys.append(pq_key)
            self.P_Keys.sort()

    def is_empty(self):
        if len(self.P_Keys) == 0:
            return True
        return False

    def get(self):
        key_pq = self.P_Keys[0]
        val_pq = self.k_v[key_pq]
        del self.k_v[key_pq]
        del self.v_k[val_pq]
        self.P_Keys = self.P_Keys[1:]
        return val_pq


