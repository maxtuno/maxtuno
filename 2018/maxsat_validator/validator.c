/*
///////////////////////////////////////////////////////////////////////////////
//        copyright (c) 2012-2018 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////
*/

#ifndef WMAXSAT_HESS_H
#define WMAXSAT_HESS_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

struct variable {
    unsigned long id;
    bool value;
};

struct clause {
    double weight;
    unsigned long size;
    struct variable *variables;
};

struct cpu {
    unsigned long i;
    unsigned long j;
    unsigned long _i_;
    unsigned long _j_;
    unsigned long n_variables;
    unsigned long n_clauses;
    long memory;
    double local;
    double global;
    double max_sat;
    struct clause *clauses;
    bool *assignment;
};

void save_state(struct cpu *cpu) {
    cpu->_i_ = cpu->i;
    cpu->_j_ = cpu->j;
}

void load_state(struct cpu *cpu) {
    cpu->i = cpu->_i_;
    cpu->j = cpu->_j_;
}

void init(const char *file_name, struct cpu *cpu) {
    char *end;
    char *buffer = calloc(32, sizeof(char));
    FILE *file = fopen(file_name, "r");
    cpu->n_variables = 0;
    cpu->n_clauses = 0;
    while (!(cpu->n_variables && cpu->n_clauses)) {
        fscanf(file, "%s", buffer);
        if (strcmp(buffer, "cnf") == 0 || strcmp(buffer, "wcnf") == 0) {
            fscanf(file, "%s", buffer);
            cpu->n_variables = strtoul(buffer, &end, 10);
            fscanf(file, "%s", buffer);
            cpu->n_clauses = strtoul(buffer, &end, 10);
        }
    }
    cpu->clauses = calloc(cpu->n_clauses, sizeof(struct clause));
    cpu->assignment = calloc(cpu->n_variables, sizeof(bool));
    for (cpu->i = 0; cpu->i < cpu->n_clauses; cpu->i++) {
        cpu->clauses[cpu->i].variables = calloc(cpu->n_variables, sizeof(struct variable));
        cpu->clauses[cpu->i].weight = 0;
        cpu->clauses[cpu->i].size = 0;
        do {
            fscanf(file, "%s", buffer);
            if (strcmp(buffer, "0") == 0) {
                break;
            }
            if (strcmp(buffer, "c") == 0) {
                fscanf(file, "%s", buffer);
                while (strcmp(buffer, "\n") == 0) {
                    break;
                }
            }
            if (!cpu->clauses[cpu->i].weight) {
                cpu->clauses[cpu->i].weight = strtod(buffer, &end);
                cpu->max_sat += cpu->clauses[cpu->i].weight;
                fscanf(file, "%s", buffer);
            }
            cpu->memory = strtol(buffer, &end, 10);
            cpu->assignment[(unsigned long) (labs(cpu->memory) - 1)] = cpu->memory % 2 == 0;
            cpu->clauses[cpu->i].variables[cpu->clauses[cpu->i].size].id = (unsigned long) (labs(cpu->memory) - 1);
            cpu->clauses[cpu->i].variables[cpu->clauses[cpu->i].size].value = cpu->memory > 0;
            cpu->clauses[cpu->i].size++;
        } while (!feof(file));
        cpu->clauses[cpu->i].variables = realloc(cpu->clauses[cpu->i].variables, cpu->clauses[cpu->i].size * sizeof(struct variable));
    }
    fclose(file);
    free(buffer);
}

void finalize(const char *file_name, struct cpu *cpu) {
    char *buffer = malloc(128 * sizeof(char));
    sprintf(buffer, "%s.hess.txt", file_name);
    FILE *sat_file = fopen(buffer, "w");
    for (cpu->i = 0; cpu->i < cpu->n_variables; cpu->i++) {
        fprintf(sat_file, "%li ", cpu->assignment[cpu->i] ? +(cpu->i + 1) : -(cpu->i + 1));
    }
    fprintf(sat_file, "0\n");
    fclose(sat_file);
    free(buffer);
    free(cpu->assignment);
    free(cpu->clauses->variables);
    free(cpu->clauses);
}

void dump(struct cpu *cpu) {
    save_state(cpu);
    /*
    printf("c www.peqnp.science\n");
    printf("c Hyper Exponential Space Sorting by Oscar Riveros mailto:contact@peqnp.science\n");
    printf("p cnf %lu %lu\n", cpu->n_variables, cpu->n_clauses);
    for (cpu->i = 0; cpu->i < cpu->n_clauses; cpu->i++) {
        printf("%lf ", cpu->clauses[cpu->i].weight);
        for (cpu->j = 0; cpu->j < cpu->clauses[cpu->i].size; cpu->j++) {
            if (cpu->clauses[cpu->i].variables[cpu->j].value) {
                printf((cpu->assignment[cpu->clauses[cpu->i].variables[cpu->j].id] ? "%lu " : "-%lu "), cpu->clauses[cpu->i].variables[cpu->j].id + 1);
            } else {
                printf((cpu->assignment[cpu->clauses[cpu->i].variables[cpu->j].id] ? "%-lu " : "%lu "), cpu->clauses[cpu->i].variables[cpu->j].id + 1);
            }
        }
        printf("0\n");
    }
     */
    printf("c \n");
    printf("c Assignment Score <%lf | %lf>\n",  cpu->local, cpu->max_sat - cpu->local);
    printf("c \n");
    load_state(cpu);
}

void load_assignment(const char *file_name, struct cpu *cpu) {
    FILE *file = fopen(file_name, "r");
    char *end;
    char *buffer = calloc(32, sizeof(char));
    fscanf(file, "%s", buffer);
    do {
        cpu->memory = strtol(buffer, &end, 10);
        cpu->assignment[labs(cpu->memory) - 1] = cpu->memory > 0;
        fscanf(file, "%s", buffer);
    } while (strcmp(buffer, "0") != 0);
    free(buffer);
    fclose(file);
}

#endif /* WMAXSAT_HESS_H */
