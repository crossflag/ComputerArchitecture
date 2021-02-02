import disassembler2
import sys


class Simulator:

    def __init__(self):
        pass

    def run(self):
        global outputFile
        global Memory
        Memory = 96

        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                inputFile = sys.argv[i + i]
            elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
                outputFile = sys.argv[i + 1]
        outputFile = open(outputFile + "_sim.txt", 'w')
        d = disassembler2.TestMe()
        d.run()

        i = 0
        cycle_counter = 0
        data_start = disassembler2.Memory
        data_rows = [data_start, data_start + 32, data_start + 64, data_start + 96]
        r_32 = [0] * 32
        data_D = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        while True:
            if disassembler2.opcodeStr[i] == "ADDI":
                num = disassembler2.arg1[i]
                r_32[int(disassembler2.arg3[i])] = r_32[num] + int(disassembler2.arg2[i])
                outputFile.write("====================" + "\n" + "cycle:" + str(cycle_counter+1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "ADDI" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write("r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                                 str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6])+ "\t" + str(r_32[7]) + "\t" + "\n" +
                                 "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                                 str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14])+ "\t" + str(r_32[15]) + "\t" + "\n" +
                                 "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                                 str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22])+ "\t" + str(r_32[23]) + "\t" + "\n" +
                                 "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                                 str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30])+ "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "B":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "B" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
                offset = disassembler2.arg3[i]
                i += offset -1
            elif disassembler2.opcodeStr[i] == "ADD":
                num = disassembler2.arg1[i]
                num2 = disassembler2.arg2[i]
                r_32[disassembler2.arg3[i]] = r_32[num] + r_32[num2]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "ADD" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "SUB":
                num = disassembler2.arg1[i]
                num2 = disassembler2.arg2[i]
                r_32[disassembler2.arg3[i]] = r_32[num] - r_32[num2]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "SUB" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "SUBI":
                num = disassembler2.arg1[i]
                r_32[int(disassembler2.arg3[i])] = r_32[num] - int(disassembler2.arg2[i])
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "SUBI" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "AND":
                r_32[disassembler2.arg3[i]] = r_32[disassembler2.arg1[i]] & r_32[disassembler2.arg2[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "AND" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "ORR":
                r_32[disassembler2.arg3[i]] = r_32[disassembler2.arg2[i]] | r_32[disassembler2.arg1[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "ORR" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "EOR":
                r_32[disassembler2.arg3[i]] = r_32[disassembler2.arg2[i]] ^ r_32[disassembler2.arg1[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "EOR" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "MOVZ":
                m_num = disassembler2.arg1[i]
                p_num = (pow(2, m_num))
                r_32[disassembler2.arg3[i]] = p_num * disassembler2.arg2[i]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "MOVZ" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr3[i])
                                 + "\t" + str(disassembler2.argStr2[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "MOVK":
                p_num = 1
                if disassembler2.arg1[i] != 0:
                    k_num = disassembler2.arg1[i]
                    p_num = (pow(2,k_num))
                temp_num = p_num * disassembler2.arg2[i]
                r_32[disassembler2.arg3[i]] = temp_num + r_32[disassembler2.arg3[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "MOVK" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr3[i])
                                 + "\t" + str(disassembler2.argStr2[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "STUR":
                store = r_32[disassembler2.arg3[i]]
                addr = r_32[disassembler2.arg1[i]] + disassembler2.arg2[i] * 4

                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "STUR" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                while addr > data_rows[-1]:
                    data_rows.append(data_rows[-1] + 32)
                    data_D.append([0, 0, 0, 0, 0, 0, 0, 0])

                for j in range(len(data_rows)):
                    if addr > data_rows[j]:
                        continue
                    elif addr < data_rows[j]:
                        row_index = j - 1
                        data_index = (addr - data_rows[row_index]) / 4
                        data_D[row_index][data_index] = store

                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")

            elif disassembler2.opcodeStr[i] == "LDUR":
                addr = r_32[disassembler2.arg1[i]] + disassembler2.arg2[i] * 4
                for t in range(len(data_rows)):
                    if addr > data_rows[t]:
                        continue
                    elif addr < data_rows[t]:
                        row_index = t - 1
                        data_index = (addr - data_rows[row_index]) / 4
                        r_32[disassembler2.arg3[i]] = data_D[row_index][data_index]
                    elif addr > data_rows[-1]:
                        print("OUT OF RANGE")
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "LDUR" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "CBZ":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" "CBZ" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
                if r_32[disassembler2.arg3[i]] == 0:
                    offset = disassembler2.arg1[i]
                    i += offset - 1
            elif disassembler2.opcodeStr[i] == "CBNZ":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "CBNZ" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
                if r_32[disassembler2.arg3[i]] != 0:
                    offset = disassembler2.arg1[i]
                    i += offset - 1
            elif disassembler2.opcodeStr[i] == "ASR":
                num1 = disassembler2.arg2[i]
                num2 = (pow(2,num1))
                r_32[disassembler2.arg3[i]] = disassembler2.arg1[i] / num1
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "ASR" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "LSL":
                num1 = disassembler2.arg2[i]
                num2 = (pow(2, num1))
                r_32[disassembler2.arg3[i]] = num2 * r_32[disassembler2.arg1[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "LSL" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "LSR":
                num1 = disassembler2.arg2[i]
                num2 = (pow(2, num1))
                r_32[disassembler2.arg3[i]] = r_32[disassembler2.arg1[i]] / num2
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "LSR" + "\t" + str(disassembler2.argStr1[i]) + "\t" + str(disassembler2.argStr2[i])
                                 + "\t" + str(disassembler2.argStr3[i]) + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "NOP":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                 + "\t" + "NOP" + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
            elif disassembler2.opcodeStr[i] == "BREAK":
                outputFile.write("====================" + "\n" + "cycle: " + str(cycle_counter + 1) + "\t" + str(disassembler2.mem[i])
                                  + "\t" + "BREAK" + "\n")
                outputFile.write("\n" + "registers:" + "\n")
                outputFile.write(
                    "r00: " + str(r_32[0]) + "\t" + str(r_32[1]) + "\t" + str(r_32[2]) + "\t" + str(r_32[3]) + "\t" +
                    str(r_32[4]) + "\t" + str(r_32[5]) + "\t" + str(r_32[6]) + "\t" + str(r_32[7]) + "\t" + "\n" +
                    "r08: " + str(r_32[8]) + "\t" + str(r_32[9]) + "\t" + str(r_32[10]) + "\t" + str(r_32[11]) + "\t" +
                    str(r_32[12]) + "\t" + str(r_32[13]) + "\t" + str(r_32[14]) + "\t" + str(r_32[15]) + "\t" + "\n" +
                    "r16: " + str(r_32[16]) + "\t" + str(r_32[17]) + "\t" + str(r_32[18]) + "\t" + str(r_32[19]) + "\t" +
                    str(r_32[20]) + "\t" + str(r_32[21]) + "\t" + str(r_32[22]) + "\t" + str(r_32[23]) + "\t" + "\n" +
                    "r24: " + str(r_32[24]) + "\t" + str(r_32[25]) + "\t" + str(r_32[26]) + "\t" + str(r_32[27]) + "\t" +
                    str(r_32[28]) + "\t" + str(r_32[29]) + "\t" + str(r_32[30]) + "\t" + str(r_32[31]) + "\t" + "\n")
                outputFile.write("\n" + "data:" + "\n")
                for row, data in zip(data_rows, data_D):
                    outputFile.write(str(row) + ": " + str(data) + "\n")
                break
            i += 1
            cycle_counter += 1
            Memory += 4
if __name__ == '__main__':
    test = Simulator()
    test.run()