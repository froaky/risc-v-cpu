from RegisterFile import RegisterFile
from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from ALU import ALU
from Pipeline import Pipeline

class CtrlUnit:

    def __init__(self, ceil_pc):
        self.pipe = Pipeline(ceil_pc)

    def pipeline(self, reg_file: RegisterFile, alu: ALU, i_mem: InstructionMemory, d_mem: DataMemory) -> dict:

        state = {}

        state['w'] = self.pipe.writeback(reg_file)
        if state['w']:
            self.pipe.MW_Buffer.clear()
        
        state['m'] = self.pipe.memory(d_mem)
        if state['m']:
            self.pipe.XM_Buffer.clear()

        state['x'] = self.pipe.execute(alu, reg_file)
        if state['x'] or type(state['x']) is int:
            self.pipe.DX_Buffer.clear()

        state['d'] = self.pipe.decode(reg_file)
        if state['d']:
            self.pipe.FD_Buffer.clear()

        state['f'] = self.pipe.fetch(reg_file, i_mem)
        
        return state

    def flush(self) -> None:
        self.pipe.FD_Buffer.clear()
        self.pipe.DX_Buffer.clear()