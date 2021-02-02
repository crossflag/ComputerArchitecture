"""Names:
Dalton Melville
Diego Santana
"""
import team12_Disassembler
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
        d = team12_Disassembler.TestMe()
        d.run()

        i = 0
        cycle_counter = 0
        data_start = team12_Disassembler.Memory
        data_rows = [data_start, data_start + 32, data_start + 64, data_start + 96]
        r_32 = [0] * 32
        data_D = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        while True:
            if team12_Disassembler.opcodeStr[i] == "ADDI":
                num = team12_Disassembler.arg1[i]
                r_32[int(team12_Disassembler.arg3[i])] = r_32[num] + int(team12_Disassembler.arg2[i])
                outputFile.write("====================" + "\n" + "cycle:" + str(cycle_counter+1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "ADDI" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "B":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "B" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
                offset = team12_Disassembler.arg3[i]
                i += offset - 1
                if i < 0:break
                elif i > len((team12_Disassembler.opcodeStr)):break
            elif team12_Disassembler.opcodeStr[i] == "ADD":
                num = team12_Disassembler.arg1[i]
                num2 = team12_Disassembler.arg2[i]
                r_32[team12_Disassembler.arg3[i]] = r_32[num] + r_32[num2]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "ADD" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "SUB":
                num = team12_Disassembler.arg1[i]
                num2 = team12_Disassembler.arg2[i]
                r_32[team12_Disassembler.arg3[i]] = r_32[num] - r_32[num2]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "SUB" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "SUBI":
                num = team12_Disassembler.arg1[i]
                r_32[int(team12_Disassembler.arg3[i])] = r_32[num] - int(team12_Disassembler.arg2[i])
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "SUBI" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "AND":
                r_32[team12_Disassembler.arg3[i]] = r_32[team12_Disassembler.arg1[i]] & r_32[team12_Disassembler.arg2[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "AND" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "ORR":
                r_32[team12_Disassembler.arg3[i]] = r_32[team12_Disassembler.arg2[i]] | r_32[team12_Disassembler.arg1[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "ORR" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "EOR":
                r_32[team12_Disassembler.arg3[i]] = r_32[team12_Disassembler.arg2[i]] ^ r_32[team12_Disassembler.arg1[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "EOR" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "MOVZ":
                m_num = team12_Disassembler.arg1[i]
                p_num = (pow(2, m_num))
                r_32[team12_Disassembler.arg3[i]] = p_num * team12_Disassembler.arg2[i]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "MOVZ" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr3[i])
                                 + "\t" + str(team12_Disassembler.argStr2[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "MOVK":
                p_num = 1
                if team12_Disassembler.arg1[i] != 0:
                    k_num = team12_Disassembler.arg1[i]
                    p_num = (pow(2,k_num))
                temp_num = p_num * team12_Disassembler.arg2[i]
                r_32[team12_Disassembler.arg3[i]] = temp_num + r_32[team12_Disassembler.arg3[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "MOVK" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr3[i])
                                 + "\t" + str(team12_Disassembler.argStr2[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "STUR":
                store = r_32[team12_Disassembler.arg3[i]]
                addr = r_32[team12_Disassembler.arg1[i]] + team12_Disassembler.arg2[i] * 4

                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "STUR" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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

            elif team12_Disassembler.opcodeStr[i] == "LDUR":
                addr = r_32[team12_Disassembler.arg1[i]] + team12_Disassembler.arg2[i] * 4
                for t in range(len(data_rows)):
                    if addr > data_rows[t]:
                        continue
                    elif addr < data_rows[t]:
                        row_index = t - 1
                        data_index = (addr - data_rows[row_index]) / 4
                        r_32[team12_Disassembler.arg3[i]] = data_D[row_index][data_index]
                    elif addr > data_rows[-1]:
                        print("OUT OF RANGE")
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "LDUR" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "CBZ":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" "CBZ" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
                if r_32[team12_Disassembler.arg3[i]] == 0:
                    offset = team12_Disassembler.arg1[i]
                    i += offset - 1
            elif team12_Disassembler.opcodeStr[i] == "CBNZ":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "CBNZ" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
                if r_32[team12_Disassembler.arg3[i]] != 0:
                    offset = team12_Disassembler.arg1[i]
                    i += offset - 1
            elif team12_Disassembler.opcodeStr[i] == "ASR":
                num1 = team12_Disassembler.arg2[i]
                num2 = (pow(2,num1))
                r_32[team12_Disassembler.arg3[i]] = team12_Disassembler.arg1[i] / num1
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "ASR" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "LSL":
                num1 = team12_Disassembler.arg2[i]
                num2 = (pow(2, num1))
                r_32[team12_Disassembler.arg3[i]] = num2 * r_32[team12_Disassembler.arg1[i]]
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "LSL" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "LSR":
                num1 = team12_Disassembler.arg2[i]
                num2 = (pow(2, num1))
                r_32[team12_Disassembler.arg3[i]] = r_32[team12_Disassembler.arg1[i]] / num2
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
                                 + "\t" + "LSR" + "\t" + str(team12_Disassembler.argStr1[i]) + "\t" + str(team12_Disassembler.argStr2[i])
                                 + "\t" + str(team12_Disassembler.argStr3[i]) + "\n")
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
            elif team12_Disassembler.opcodeStr[i] == "NOP":
                outputFile.write("====================" + "\n" + "cycle " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
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
            elif team12_Disassembler.opcodeStr[i] == "BREAK":
                outputFile.write("====================" + "\n" + "cycle: " + str(cycle_counter + 1) + "\t" + str(team12_Disassembler.mem[i])
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