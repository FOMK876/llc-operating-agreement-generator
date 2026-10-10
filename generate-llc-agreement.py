import os 

template = """
LIMITED LIABILITY COMPANY OPERATING AGREEMENT

THIS Operating Agreement is made and entered into on this ___ day of ________, 20XX, by and between the Members of the Limited Liability Company known as _______________ LLC (the "Company"). This agreement sets forth the terms of the Company's organization, the rights and obligations of its members, and the rules for the company's management.

1. FORMATION AND PURPOSE
1.1 The Company was formed in accordance with the Limited Liability Company Act of the State of ___________. 
1.2 The principal purpose of the Company is to engage in any lawful business activity permitted under the law of the State of ___________, including but not limited to: _________________.

2. MEMBERS
2.1 The initial Members of the company are:
[Member Name 1]
[Member Name 2]
2.2 The transfer of membership interests to any person not currently a member shall require the written consent of the existing members holding a majority of the Percentage Interests.

3. CAPITAL CONTRIBUTIONS
3.1 The initial total contribution of the Members to the capital of the Company shall be $100. 
3.2 Each Member's capital contribution is to be made in cash, which shall be credited to the capital account of each respective Member. 

4. PROFIT AND LOSS ALLOCATIONS
4.1 The Net Profits and Losses of the Company shall be allocated among the Members in proportion to their respective Percentage Interests in the Company at the time the Net Profits or Losses are determined.
- [Member Name 1]: ___%
- [Member Name 2]: ___%

5. DISTRIBUTIONS
5.1 The financial statements of the Company shall be prepared and available to each Member within ___ days following the close of each calendar year.
5.2 Distributions of Net Profits shall be made at such times as determined by the Members, in proportion to their respective Percentage Interests.

6. MANAGEMENT
6.1 The Company shall be managed by: (Check one)
[ ] Manager-Managed: The Company shall be managed by one or more Managers appointed by the Members. 
[ ] Member-Managed: The Company shall be managed by the Members.
6.2 Voting: [Describe how voting works, e.g., majority of percentage interests or one-person-one-vote]

7. DISSOLUTION
7.1 The Company shall dissolve upon:
a) The written consent of Members holding a majority of the voting interests.
b) The entry of a decree of judicial dissolution.

***

DISCLAIMER: This document is a general template only and does not constitute legal advice. The rules governing Limited Liability Companies vary significantly by State. This template may not cover all applicable legal requirements, specific state regulations, or nuances in your business model. Before using this document or beginning an LLC, you should consult with a licensed attorney to ensure your Operating Agreement fully protects your personal assets and complies with the applicable state laws.

==============================================
NOTICE OF CUSTOM SERVICE:
==============================================
If you require a complete, legally custom-tailored operating agreement specific to your State, your unique Management Structure, and your specific member vesting schedule, you can purchase the "LLC Agreement Forge" professional service.
Visit: https://harvst.online/mind-llc-agreement-forge-20261008-0815
"""

def main():
    file_name = 'llc_operating_agreement_template.txt'
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(template)
        print(f"Success: Generated LLC Operating Agreement template.")
        print(f"File created at your current directory.")
    except Exception as e:
        print(f"Error: Failed to write file. {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()

