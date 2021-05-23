# mop
MOP Telegram

List group members.
Multiple groups.
Loop.  
Extract duplicates and increment
List duplicate and group.

Input:
- telegram groups with potential duplicate members

Output:
- spreadsheet
- each column contains a group name as the title
- each column lists group members
- the duplicate members are listed at the end of each group list with duplicate as a "sub title"
- a summary page with groups as rows and the unique member count
- summary page includes total number of unique members
- lists duplicate members and frequency of occurrence.

iteration 0: display group name and list all members in the group.  store as a CSV
iteration 1: perform 0 for multiple groups as listed as input. store each as a CSV row
iteration 2: as we loop thru each group, isolate and increment duplicates, store in a CSV named multiples.
iteration 3: merge duplicates in each group at the bottom of each list.
iteration 4: as we perform 2, we output summary data into another CSV.

members CSV
----------------------
i, group i
i+1, member i
member i+1
count0
duplicates
duplicate i
duplicate i+1
count1
total0

summary CSV
----------------------
group i, count_all i, count_unique i

duplicate i, count i
