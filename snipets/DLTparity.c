#include <stdio.h>
#include <string.h>

char generate_parity_bit(char data[])
{
    int count_ones = 0;
    int length = strlen(data);

    for (int i = 0; i < length; i++)
    {
        if (data[i] == '1')
        {
            count_ones++;
        }
    }
    if (count_ones % 2 == 0)
    {
        return '0';
    }
    else
    {
        return '1';
    }
}

int check_parity(char data[])
{
    int count_ones = 0;
    int length = strlen(data);

    for (int i = 0; i < length - 1; i++)
    {
        if (data[i] == '1')
        {
            count_ones++;
        }
    }
    if ((count_ones % 2 == 0 && data[length - 1] == '0') || (count_ones % 2 != 0 && data[length - 1] == '1'))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int choice;
    char input_data[32];
    char parity_bit;

    while (1)
    {
        printf("\nMenu:\n");
        printf("1. Generate Parity\n");
        printf("2. Parity Checker\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            printf("Enter input data (max 32 bits): ");
            scanf("%s",&input_data);

            parity_bit = generate_parity_bit(input_data);
            printf("Generated Parity Bit: %c\n", parity_bit);

            printf("Data with Parity Bit: %s%c", input_data, parity_bit);
        }
        else if (choice == 2)
        {
            printf("Enter input data with parity bit: ");
            scanf("%s",&input_data);

            int parity_check_result = check_parity(input_data);

            if (parity_check_result)
            {
                printf("Parity Check: Passed\n");
            }
            else
            {
                printf("Parity Check: Failed\n");
            }
        }
        else if (choice == 3)
        {
            printf("Exiting the program.\n");
            break;
        }
        else
        {
            printf("Invalid choice. Please enter a valid choice.\n");
        }
    }
    return 0;
}
