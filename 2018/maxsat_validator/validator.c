/*
///////////////////////////////////////////////////////////////////////////////
//        copyright (c) 2012-2018 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////
*/

#include "validator.h"

void functor(struct cpu *cpu) {
    save_state(cpu);
    cpu->local = cpu->max_sat;
    for (cpu->i = 0; cpu->i < cpu->n_clauses; cpu->i++) {
        cpu->memory = 0;
        for (cpu->j = 0; cpu->j < cpu->clauses[cpu->i].size; cpu->j++) {
            cpu->memory += cpu->clauses[cpu->i].variables[cpu->j].value == cpu->assignment[cpu->clauses[cpu->i].variables[cpu->j].id];
            if (cpu->memory) {
                break;
            }
        }
        cpu->local -= cpu->clauses[cpu->i].weight * cpu->memory;
    }
    load_state(cpu);
}

int main(int argc, char const *argv[]) {
    struct cpu cpu;
    init(argv[1], &cpu);

    /* begin validator only */
    load_assignment(argv[2], &cpu);
    functor(&cpu);
    dump(&cpu);
    free(cpu.assignment);
    free(cpu.clauses->variables);
    free(cpu.clauses);
    /* end validator only */

    /* Hyper Exponential Space Sorting */
    /* hess(&cpu); */
    /* finalize(argv[1], &cpu); */

    return 0;
}
