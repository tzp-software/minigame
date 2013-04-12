'''
    minigame.minigame.locker.py

    use to lock files

'''

class FileLocker(object):
    ''' use to lock files
    should be imported as somthing
    ie: import FileLocker as DieLocker'''
    def __init__(self):
        self.lock = [][:]

    def __str__(self):
        if len(self.lock) > 0:
            ret = ', '.join(map(str, self.lock))
        else:
            ret = 'No items locked'

        return ret

    def __len__(self):
        return len(self.lock)

    def lock(self, item):
        if item not in self.lock:
            self.lock.append(item)
        else:
            print '{0} is already locked'.format(item)

    def unlock(self, item):
        if item in self.lock:
            self.lock.remove(item)
        else:
            print '{0} is not currently locked'.format(item)

    
