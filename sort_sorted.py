a = {'8d0922e8-5f2e-4f74-a2d6-4482ba841057': 37, 'acdd4042-a069-4b6c-82e3-9060c6d41067': 5,
     'f88e8ba4-229d-4ee1-81e0-9885a6a9edc5': 20, '647dfecd-39ee-44e5-a609-7bd91d50be56': 57,
     '7d668345-1e4e-4bca-babb-6909307288cd': 32, '3255be25-c822-4f57-8801-26798975fc8a': 19,
     '072e6fff-de07-48e2-85d5-38ca4f95ab5f': 16, 'internal': 32, '4c0ce117-0f37-438a-81ee-304ef8a17a2f': 29,
     '1248cbfc-f5c6-40fc-93b7-38e205b628f2': 8, '774a77f6-003b-4062-8f35-ebc44f57caab': 15,
     '93215cc1-fe0f-4095-91cb-61a82418d168': 9, 'ca2d86da-969b-46a7-9872-26b4f4ff8ce3': 3,
     '77323a8d-e667-4da0-8b6e-1badde4b70da': 6, '796f2610-ee58-47ef-9683-eae4a22afcb8': 2,
     '144b4383-1e04-4acf-b406-5c0bb7a5f97d': 9, '6c9277cf-af5a-4a26-9384-50690abaf00a': 2,
     '7a73f351-bce2-4547-933c-7089a80a2580': 3, 'ba2254bd-b78f-4332-9334-73a547f7d6e1': 4,
     'd941509d-afab-4f1e-ac09-70d36610ad2d': 7, '6777765c-4c0a-4418-95b1-827a1181fb38': 1,
     '36e09209-028a-41ca-a172-ad3287ca5005': 4, '28a9de9f-940d-497a-b68a-1a120aeab619': 8,
     '2b18a8af-a756-4c86-9ec4-ad0cf18375f1': 4, '6ab281be-49e4-4607-aeac-586bac5feb42': 1,
     '0993c991-4121-4d63-a49d-99b2e7a7600e': 5, 'efa1fa9d-4b38-4f92-891a-9c40eb743c4a': 3,
     '557a527d-1756-4a4f-9f4f-fc4928c38ff6': 1, '22a932c5-75e4-48a9-800b-2f731209000b': 4,
     '16ec7fe1-4b31-407f-a760-0456f17edc2c': 1, '4c5279f2-8d5e-44e3-8728-9befaea4b8f5': 2,
     '3b5b417a-3d98-4afb-ac74-9b5c906c022d': 1}
b = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
print(b)


cc = [(6,2), (4,3), (2,6), (2,3), (1,5)]

cc.sort(key=lambda x : (x[0], x[1]))
print(cc)