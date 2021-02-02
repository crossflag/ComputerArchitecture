import team12_Disassembler
import sys

cycle = 0
pre_issue_buff = [-1, -1, -1, -1]
pre_alu_buff = [-1, -1]
pre_mem_buff = [-1, -1]
post_mem_buff = [-1, -1]
post_alu_buff = [-1]
r = [0] * 32


class Simulator:
    class WB:

        def __init__(self):
            pass

        @staticmethod
        def run():

            if post_alu_buff[1] != -1:
                r[post_alu_buff[1]] = post_alu_buff[0]
                post_alu_buff[0] = -1
                post_alu_buff[1] = -1
            if post_mem_buff[1] != -1:
                r[post_mem_buff[1]] = post_mem_buff[0]
                post_mem_buff[0] = -1
                post_mem_buff[1] = -1

    def __init__(self, instrs, opcodes, mem, addrs,
                 arg1, arg2, arg3, num_instrs, dest, src1, src2, cycle):
        self.instrs = instrs
        self.opcodes = opcodes
        self.mem = mem
        self.addrs = addrs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.num_instrs = num_instrs
        self.dest = dest
        self.src1 = src1
        self.src2 = src2
        self.cycle = cycle

    def print_state(self, output_file):
        output_file.write( "Cycle: " + str( cycle ) + "\n" )
        output_file.write( "Pre-Issue Buffer:" + "\n" )
        for i in range( len( pre_issue_buff ) ):
            output_file.write( "Entry " + str( i ) + ":" + str( pre_issue_buff[i] ) + "\n" )
        output_file.write( "Pre_ALU Queue:" + "\n" )
        for i in range( len( pre_alu_buff ) ):
            output_file.write( "Entry " + str( i ) + ":" + str( pre_alu_buff[i] ) + "\n" )
        output_file.write( "Post_ALU Queue:" + "\n" )
        for i in range( len( post_alu_buff ) ):
            output_file.write( "Entry " + str( i ) + ":" + str( post_alu_buff[i] ) + "\n" )
        output_file.write( "Pre_MEM Queue:" + "\n" )
        for i in range( len( pre_mem_buff ) ):
            output_file.write( "Entry " + str( i ) + ":" + str( pre_mem_buff[i] ) + "\n" )
        output_file.write( "Post_MEM Queue:" + "\n" )
        for i in range( len( post_mem_buff ) ):
            output_file.write( "Entry " + str( i ) + ":" + str( post_mem_buff[i] ) + "\n" )
        output_file.write( "Registers:" + "\n" )
        output_file.write( "R00:" + "\t" )
        for i in range( len( r ) ):
            if i == 8 or i == 16 or i == 24:
                output_file.write( "\n" )
                if i == 8:
                    output_file.write( "R0" + str( i ) + "\t" )
                else:
                    output_file.write( "R" + str( i ) + "\t" )
            output_file.write( str( r[i] ) + "\t" )

    def run(self):

        for i in range( len( sys.argv ) ):
            if sys.argv[i] == '-i' and i < (len( sys.argv ) - 1):
                input_file = sys.argv[i + i]
            elif sys.argv[i] == '-o' and i < (len( sys.argv ) - 1):
                output_file = sys.argv[i + 1]

        output_file = open( output_file + "_sim.txt", 'w' )

        tester = True
        while tester:
            self.WB.run()
            self.ALU.run()
            self.print_state( output_file )
            self.cycle += 1
            tester = False
    class IssueBuffer:

        def __init__(self):
            pass

        @staticmethod
        def run():
            print ("UNDER CONSTRUCTION")


    class MEM:

        def __init__(self):
            pass

        @staticmethod
        def run():
            print("Do the damn thing")

    class ALU:

        def __init__(self):
            pass

        @staticmethod
        def run(self):
            if not pre_alu_buff:
                pre_alu_buff.append(pre_issue_buff[0])
                pre_alu_buff.append(pre_issue_buff[1])

                if not post_alu_buff:
                    post_alu_buff.append(pre_alu_buff[0])
                    pre_alu_buff[0] = pre_alu_buff[1]
                    pre_alu_buff[1] = " "

                    #not sure what variables will be yet but here is basic arithmetic
                    if post_alu_buff[0] == "ADDI":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] + self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                    elif post_alu_buff[0] == "B":
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "ADD":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] + self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "SUB":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] - self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "SUBI":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] - self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "AND":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] & self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "ORR":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] | self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "EOR":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] ^ self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "MOVZ":
                        p_num = pow(2,self.src1[post_alu_buff[0]])
                        r[self.dest[post_alu_buff[0]]] = p_num * self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "MOVK":
                        p_num = pow(2, self.src1[post_alu_buff[0]])
                        r[self.dest[post_alu_buff[0]]] = p_num * self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0] )
                    elif post_alu_buff[0] == "STUR":
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "LDUR":
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0])
                    elif post_alu_buff[0] == "CBZ":
                        if r[self.dest[post_alu_buff[0]]] == 0:
                            offset = self.src1[post_alu_buff[0]]
                            self.dest[post_alu_buff[0]] += offset - 1
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0] )
                    elif post_alu_buff[0] == "CBNZ":
                        if r[self.dest[post_alu_buff[0]]] != 0:
                            offset = self.src1[post_alu_buff[0]]
                            self.dest[post_alu_buff[0]] += offset - 1
                        post_alu_buff[0] = post_alu_buff.append( pre_alu_buff[0] )
                    elif post_alu_buff[0] == "ASR":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] / self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                    elif post_alu_buff[0] == "LSL":
                        p_num = pow(2, self.src2[post_alu_buff[0]])
                        r[self.dest[post_alu_buff[0]]] = p_num * self.src1[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                    elif post_alu_buff[0] == "LSR":
                        r[self.dest[post_alu_buff[0]]] = self.src1[post_alu_buff[0]] / self.src2[post_alu_buff[0]]
                        post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                    elif post_alu_buff[0] == "NOP":
                        post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                    elif post_alu_buff[0] == "BREAK":
                        post_alu_buff[0] = post_alu_buff.append(pre_alu_buff[0])
                    else:
                        print ("ERROR INSTRUCTION NOT RECOGNIZED")








if __name__ == "__main__":
    d = team12_Disassembler.TestMe()
    d.run()
    s = Simulator( team12_Disassembler.instructions, team12_Disassembler.opcodeStr, team12_Disassembler.mem, team12_Disassembler.addrs,
                   team12_Disassembler.arg1,
                   team12_Disassembler.arg2, team12_Disassembler.arg3, team12_Disassembler.numInstrs, team12_Disassembler.dest, team12_Disassembler.src1,
                   team12_Disassembler.src2, 0 )
    s.run()




