import datetime

class Journal:


    class ProtocolUnit:

        def __init__(self, start_time: datetime.timedelta, command: str):
            self.start_time = start_time
            self.command = command

        def __str__(self):
            days = self.start_time.total_seconds() // (24*60*60)
            hours = self.start_time.total_seconds() // (60*60) - days*24
            minutes = self.start_time.total_seconds() // 60 - hours*60 - days*24*60
            return f"{int(hours)}:{int(minutes)} {self.command}"


    def __init__(self, file_name="input.txt"):

        self.time_needed_of_command = dict()
        self.journal = list()
        self.protocol = list()
        
        with open(file_name) as file:
            n = int(file.readline())
            for _ in range(n):
                command, time_needed = file.readline().strip().split()
                time_needed = datetime.timedelta(minutes=int(time_needed))
                self.time_needed_of_command[command] = time_needed
            self.time_needed_of_command["DEL"] = datetime.timedelta(0)
            
            line = file.readline().strip()
            while line:
                self.journal.append(line)
                line = file.readline().strip()

        self.__make_protocol()

    def __make_protocol(self):

        cur_line_num = 0
        while True: # Добавляем 1 элемент, не являющийся "DEL"
            time, command = self.journal[cur_line_num].split()
            time = datetime.timedelta(hours=int(time[:2]), minutes=int(time[3:]))
            cur_line_num += 1
            if command != "DEL":
                self.__add_to_protocol(time, command)
                break

        start = cur_line_num
        stop = len(self.journal)
        for line_num in range(start, stop):

            time, command = self.journal[line_num].split()
            time = datetime.timedelta(hours=int(time[:2]), minutes=int(time[3:]))

            if self.protocol:
                prev_cmnd_end_time = self.protocol[-1].start_time \
                    + self.time_needed_of_command[self.protocol[-1].command]
            else:
                prev_cmnd_end_time = datetime.timedelta(hours=0, minutes=0)

            if self.protocol and command == "DEL" and prev_cmnd_end_time >= time:
                del self.protocol[-1]
            elif self.protocol and prev_cmnd_end_time > time:
                self.__add_to_protocol(prev_cmnd_end_time, command)
            else:
                self.__add_to_protocol(time, command)

        if self.protocol:
            last_cmnd_end_time = self.protocol[-1].start_time \
                + self.time_needed_of_command[self.protocol[-1].command]
            self.__add_to_protocol(last_cmnd_end_time, "")
        
    def __add_to_protocol(self, start_time: datetime.timedelta, command: str):
        self.protocol.append(Journal.ProtocolUnit(start_time, command))

    def save_protocol(self, file_name="output.txt"):
        with open(file_name, "w") as file:
            for line in self.protocol:
                file.write(f"{str(line).strip()}\n")

a = Journal()
a.save_protocol()