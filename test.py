txt = """
      "hash": "EA70B32C55C193345D625F766EEA2FCA52D3F2CCE0B3A30838CC543026BB0FEA",
      "duration": "4000",
      "time": "1544819986",
      "tally": "80394786589602980996311817874549318248",
      "blocks": "1", // since V21.0
      "voters": "37", // since V21.0
      "request_count": "2" // since V20.0
"""
x = []
for i in txt.split("\n"):
    x.append(i[:i.find(":")+1]+f"response[{i[:i.find(':')].replace(' ','')}]")


x = "\n".join(x)
print(x)